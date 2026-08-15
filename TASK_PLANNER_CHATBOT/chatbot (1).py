import datetime
import re
import csv

# Represents a single task with a title and an optional deadline.
class Task:

    def __init__(self, title, deadline=None):
        self.title = title
        self.deadline = deadline

    def priority_label(self):
        if not self.deadline:
            return "low"
        now = datetime.datetime.now()
        delta = (self.deadline - now).total_seconds()
        days = delta / 86400  
        if days < 0:
            return "high"
        elif days <= 2:
            return "high"  
        elif days <= 7:
            return "normal"
        else:
            return "low"

    def is_overdue(self):
        if self.deadline and datetime.datetime.now() > self.deadline:
            return True
        return False

    def deadline_str(self):
        if self.deadline:
            return self.deadline.strftime("%Y-%m-%d %H:%M")
        return None

    def priority_sort_value(self):
        return self.deadline.timestamp() if self.deadline else float('inf')


# Analyize a time string.
def get_time(text):

    text = text.strip().lower()
    match = re.match(r"(\d{1,2})(:(\d{2}))?\s*(am|pm)?", text)
    if not match:
        return None
    hour = int(match.group(1))
    minute = int(match.group(3)) if match.group(3) else 0
    ampm = match.group(4)

    if ampm == "pm" and hour != 12:
        hour += 12
    if ampm == "am" and hour == 12: 
        hour = 0
    if 0 <= hour < 24 and 0 <= minute < 60:
        return hour, minute
    return None


# Break-down a natural language string into a datetime object.
def get_deadline(text):
    now = datetime.datetime.now()
    text = text.strip().lower()

    if "today" in text:
        time_part = text.replace("today", "").strip()
        if time_part:
            t = get_time(time_part)
            if t:
                return now.replace(hour=t[0], minute=t[1], second=0, microsecond=0)
        return now.replace(hour=23, minute=59, second=59, microsecond=0)

    if "tomorrow" in text:
        tmr = now + datetime.timedelta(days=1)
        time_part = text.replace("tomorrow", "").strip()
        if time_part:
            t = get_time(time_part)
            if t:
                return tmr.replace(hour=t[0], minute=t[1], second=0, microsecond=0)
        return tmr.replace(hour=23, minute=59, second=59, microsecond=0)

    parts = text.split()
    if parts:
        # Always check for a date first!
        date_part = parts[0]
        time_part = " ".join(parts[1:]) if len(parts) > 1 else ""

        # Handle dateonly and date-time
        if re.match(r"\d{1,2}/\d{1,2}/\d{4}$", date_part):
            try:
                day, month, year = map(int, date_part.split("/"))
                if not (1 <= day <= 31 and 1 <= month <= 12):
                    return None
                dt = datetime.datetime(year, month, day, 23, 59, 59)
                if time_part:  # If there's a time after the date, parse and set it
                    t = get_time(time_part)
                    if t:
                        dt = dt.replace(hour=t[0], minute=t[1], second=0)
                return dt
            except:
                return None

    # Only time given (e.g. "6pm"), after checking date
    if len(parts) == 1 and get_time(parts[0]):
        t = get_time(parts[0])
        return now.replace(hour=t[0], minute=t[1], second=0, microsecond=0)


    return None


# Manages the collection of tasks and user interactions.
class TaskManager:

    # Save list to CSV file
    def save_list_to_csv(self, filename="tasks.csv"):
        with open(filename, mode="w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Title", "Deadline", "Priority", "Overdue"])
            for task in self.tasks:
                writer.writerow([
                    task.title,
                    task.deadline_str() if task.deadline else "",
                    task.priority_label(),
                    "YES" if task.is_overdue() else "NO"
                ])

    # Clear data of CSV file
    def clear_csv(self, filename="tasks.csv"):
        with open(filename, mode="w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Title", "Deadline", "Priority", "Overdue"])
        print(f"CSV file '{filename}' cleared.\n")

    # Initializes the manager with empty task lists.
    def __init__(self):
        self.tasks = []  
        self.pending_overdue_tasks = [] 

    # Finds a task by its title (case-insensitive).
    def find_task(self, title):
        
        for task in self.tasks:
            if task.title.lower() == title.lower():
                return task
        return None

    # Prints a formatted list of all tasks, sorted by due date.
    def show_list(self):

        if not self.tasks:
            print("No tasks mentioned yet!\n")
            return
        sorted_tasks = sorted(self.tasks, key=lambda t: t.priority_sort_value())
        print("Task Dashboard:")
        for task in sorted_tasks:
            msg = f"- {task.title}"
            if task.deadline:
                msg += f" [due: {task.deadline_str()}] (priority: {task.priority_label()})"
                if task.is_overdue():
                    msg += " **OVERDUE**"
            else:
                msg += f" (priority: {task.priority_label()})"
            print(msg)
        print()

    # Adds a new task to the list.
    def add_task(self, text):
        title = text
        deadline = None
        if " due " in text:
            parts = text.split(" due ", 1)
            title = parts[0].strip()
            deadline = get_deadline(parts[1].strip())

        # If task already exists
        for existing_task in self.tasks:
            if existing_task.title.lower() == title.lower() and not existing_task.is_overdue():
                print(f"A task named '{title}' already exists. Want to update/skip adding task?")
                reply = input("You: ").replace("You: ", "").lower()
                if reply == "update":
                    self.update_task(existing_task.title)
                    print()
                    return
                elif reply == "skip":
                    print("Skipped adding new task.\n")
                    return
                else:
                    print("Invalid reply, skipping.\n")
                    return

        # No duplicate found, add normally
        task = Task(title=title, deadline=deadline)
        self.tasks.append(task)
        print("Task added. See the updated list? (Yes/No)\n")
        self.save_list_to_csv()


    # Removes a task by its title.
    def remove_task(self, title):

        task = self.find_task(title)
        if task:
            self.tasks.remove(task)
            print(f"Task '{title}' removed. See the updated list? (Yes/No)\n")
        else:
            print(f"Task '{title}' not found.\n")
        self.save_list_to_csv()

    # Updates the deadline of an existing task.
    def update_task(self, title):

        task = self.find_task(title)
        if not task:
            print(f"Task '{title}' not found.\n")
            return
        print("Enter new deadline: ")
        new_dl = input("You: ").replace("You: ", "")
        deadline = get_deadline(new_dl)
        task.deadline = deadline
        print("Deadline updated. See the updated list? (Yes/No)\n")
        self.save_list_to_csv()

    # Fills the pending queue with overdue tasks.
    def queue_overdue_tasks(self):
        self.pending_overdue_tasks = [task for task in self.tasks if task.is_overdue()]

    # Interactively handles the next overdue task from the queue.
    def handle_next_overdue_task(self):

        if self.pending_overdue_tasks:
            task = self.pending_overdue_tasks.pop(0)
            print(f"Your task '{task.title}' is overdue (was due {task.deadline_str()}). Want to update/remove/skip?")
            reply = input("You: ").replace("You: ", "").lower()
            if reply == "update":
                self.update_task(task.title)
            elif reply == "remove":
                self.remove_task(task.title)
            elif reply == "skip":
                print("Skipped taking asking")
            print()
            return True 
        return False 


# The main function to run the chatbot interface.
def chatbot():
    bot = TaskManager()
    print("Hello! I am your Task & Time Planner AI.\n")
    pending_overdue_mode = False

    while True:
        
        if pending_overdue_mode:
            if not bot.handle_next_overdue_task():
                pending_overdue_mode = False 
            continue

        print()
        user_input = input("You: ").replace("You: ", "").strip().lower()

        if user_input.startswith("add "):
            bot.add_task(user_input[4:])
        elif user_input.startswith("remove "):
            bot.remove_task(user_input[7:])
        elif user_input.startswith("update "):
            bot.update_task(user_input[7:])
        elif user_input == "show list":
            bot.show_list()
            bot.queue_overdue_tasks()
            if bot.pending_overdue_tasks:
                pending_overdue_mode = True
        elif user_input == "clear csv":
            bot.clear_csv()         
        elif user_input == "yes":
            bot.show_list()
            bot.queue_overdue_tasks()
            if bot.pending_overdue_tasks:
                pending_overdue_mode = True
        elif user_input == "no":
            print("Okay.\n")
        elif user_input == "exit":
            print("Goodbye.")
            break
        else:
            print("Unknown command. Use: add, remove, update, show list, clear csv, exit.\n")


# Main execution block.
if __name__ == "__main__":
    chatbot()