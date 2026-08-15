import java.io.*;
import java.util.*;

class records {

    static class basics {
        String name;
        int enroll;
        String dept;
        int sem;
        String div;

        Scanner sc = new Scanner(System.in);

        void get_basics() {
            System.out.println("\nBASIC DETAILS..");
            System.out.print("Enter name: ");
            name = sc.nextLine();

            System.out.print("Enter enrollment number: ");
            enroll = sc.nextInt();
            sc.nextLine();

            System.out.print("Enter department: ");
            dept = sc.nextLine();

            System.out.print("Enter semester: ");
            sem = sc.nextInt();
            sc.nextLine();

            System.out.print("Enter division: ");
            div = sc.nextLine();
        }

        void disp_basics() {
            System.out.println("\nBASIC DETAILS:");
            System.out.println("Name: " + name);
            System.out.println("Enrollment: " + enroll);
            System.out.println("Department: " + dept);
            System.out.println("Semester: " + sem);
            System.out.println("Division: " + div);
        }
    }

    static class personal {
        String email, contact, gender, dob, address;

        Scanner sc = new Scanner(System.in);

        void get_personal() {
            System.out.println("\nPERSONAL DETAILS..");
            System.out.print("Enter email: ");
            email = sc.nextLine();

            System.out.print("Enter contact number: ");
            contact = sc.nextLine();

            System.out.print("Enter gender: ");
            gender = sc.nextLine();

            System.out.print("Enter birth date: ");
            dob = sc.nextLine();

            System.out.print("Enter address: ");
            address = sc.nextLine();
        }

        void disp_personal() {
            System.out.println("\nPERSONAL DETAILS:");
            System.out.println("Email: " + email);
            System.out.println("Contact: " + contact);
            System.out.println("Gender: " + gender);
            System.out.println("DOB: " + dob);
            System.out.println("Address: " + address);
        }
    }

    static class result {
        float[] spi;
        float cgpi;
        String grade, remark;
        int sem;

        Scanner sc = new Scanner(System.in);

        result(int sem) {
            this.sem = sem;
            spi = new float[sem - 1];
        }

        void get_result() {
            float total = 0;

            System.out.println("\nRESULT DETAILS..");

            for (int i = 0; i < sem - 1; i++) {
                System.out.print("Enter SPI for semester " + (i + 1) + ": ");
                spi[i] = sc.nextFloat();
                total += spi[i];
            }

            cgpi = sem > 1 ? total / (sem - 1) : 0;

            if (cgpi >= 9.0)
                grade = "A+";
            else if (cgpi >= 8.0)
                grade = "A";
            else if (cgpi >= 7.0)
                grade = "B+";
            else if (cgpi >= 6.0)
                grade = "B";
            else if (cgpi >= 5.0)
                grade = "C";
            else if (cgpi >= 4.0)
                grade = "D";
            else
                grade = "F";

            switch (grade) {
                case "A+":
                    remark = "Outstanding performance.";
                    break;

                case "A":
                    remark = "Excellent work.";
                    break;

                case "B+":
                    remark = "Very good.";
                    break;

                case "B":
                    remark = "Good, but can improve.";
                    break;

                case "C":
                    remark = "Average.";
                    break;

                case "D":
                    remark = "Below average.";
                    break;

                default:
                    remark = "Poor. Needs improvement.";
                    break;
            }
        }

        void disp_result() {
            System.out.println("\nRESULT DETAILS:");

            for (int i = 0; i < sem - 1; i++) {
                System.out.println("SPI Semester " + (i + 1) + ": " + spi[i]);
            }

            System.out.printf("CGPI: %.2f\n", cgpi);
            System.out.println("Grade: " + grade);
            System.out.println("Remark: " + remark);
        }
    }
}

public class student {

    records.basics b;
    records.personal p;
    records.result r;

    void get_data() {
        b = new records.basics();
        b.get_basics();

        p = new records.personal();
        p.get_personal();

        r = new records.result(b.sem);
        r.get_result();
    }

    void show_data() {
        b.disp_basics();
        p.disp_personal();
        r.disp_result();
    }

    void insert() {
        get_data();

        try (PrintWriter pw = new PrintWriter(
                new FileWriter("students.txt", true))) {

            pw.println("Enrollment: " + b.enroll);
            pw.println("Name: " + b.name);
            pw.println("Department: " + b.dept);
            pw.println("Semester: " + b.sem);
            pw.println("Division: " + b.div);
            pw.println("Email: " + p.email);
            pw.println("Contact: " + p.contact);
            pw.println("Gender: " + p.gender);
            pw.println("DOB: " + p.dob);
            pw.println("Address: " + p.address);

            for (int i = 0; i < b.sem - 1; i++) {
                pw.println("SPI Sem " + (i + 1) + ": " + r.spi[i]);
            }

            pw.printf("CGPI: %.2f\n", r.cgpi);
            pw.println("Grade: " + r.grade);
            pw.println("Remark: " + r.remark);
            pw.println("=====================================================");

        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }

    void display() {
        try (Scanner sc = new Scanner(new File("students.txt"))) {

            if (!sc.hasNextLine()) {
                System.out.println("No records found.");
                return;
            }

            System.out.println("\n--- STUDENT RECORDS ---");

            while (sc.hasNextLine()) {
                String line = sc.nextLine();

                if (line.equals("=====================================================")) {
                    System.out.println(line);
                    continue;
                }

                System.out.println(line);
            }

        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }

    void delete(int roll) {
        boolean found = false;

        File file = new File("students.txt");
        File temp = new File("temp.txt");

        try (Scanner sc = new Scanner(file);
             PrintWriter pw = new PrintWriter(temp)) {

            while (sc.hasNextLine()) {
                String line = sc.nextLine();

                if (line.equals("Enrollment: " + roll)) {
                    found = true;

                    for (int i = 0; i < 17; i++)
                        if (sc.hasNextLine())
                            sc.nextLine();

                } else {
                    pw.println(line);
                }
            }

        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }

        file.delete();
        temp.renameTo(file);

        if (found)
            System.out.println("Student deleted successfully.");
        else
            System.out.println("Student not found.");
    }

    void update(int roll) {
        delete(roll);
        insert();
    }

    void search(int roll) {
        boolean found = false;

        try (Scanner sc = new Scanner(new File("students.txt"))) {

            while (sc.hasNextLine()) {
                String line = sc.nextLine();

                if (line.equals("Enrollment: " + roll)) {
                    found = true;

                    System.out.println(line);

                    for (int i = 0; i < 16; i++) {
                        if (sc.hasNextLine())
                            System.out.println(sc.nextLine());
                    }

                    break;
                }
            }

            if (!found)
                System.out.println("Student not found.");

        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }

    public static void main(String[] args) {

        student s = new student();
        Scanner sc = new Scanner(System.in);

        while (true) {

            System.out.println("\n--- MENU ---");
            System.out.println("1. Insert");
            System.out.println("2. Delete");
            System.out.println("3. Update");
            System.out.println("4. Search");
            System.out.println("5. Display");
            System.out.println("6. Exit");

            System.out.print("Enter your choice: ");
            int ch = sc.nextInt();

            switch (ch) {

                case 1:
                    s.insert();
                    break;

                case 2:
                    System.out.print("Enter enrollment no. to delete: ");
                    s.delete(sc.nextInt());
                    break;

                case 3:
                    System.out.print("Enter enrollment no. to update: ");
                    s.update(sc.nextInt());
                    break;

                case 4:
                    System.out.print("Enter enrollment no. to search: ");
                    s.search(sc.nextInt());
                    break;

                case 5:
                    s.display();
                    break;

                case 6:
                    System.out.println("Exiting...");
                    return;

                default:
                    System.out.println("Invalid choice!");
            }
        }
    }
}