# Blackjack Game

## Description

This is a simple **console-based Blackjack game developed using Python**. The game allows a player to play Blackjack against the computer (dealer).

The program is divided into three main functions:

### 1. `card()`

This function contains a list of possible card values used in the game. It uses Python's `random` module to randomly select and return a card value.

### 2. `calc_handvalue(hand)`

This function calculates the total value of the cards in a player's or computer's hand.

In Blackjack, the Ace can have a value of **11 or 1**. If the total hand value becomes greater than 21 and an Ace with value 11 is present, it is changed to 1. The final hand value is then returned.

### 3. `blackjack()`

This function contains the main logic of the game.

* The player and computer are each given two cards.
* The player's cards and score are displayed.
* The computer's first card is displayed.
* The player can choose to **hit** or **stand**.
* If the player chooses **hit**, another card is added to their hand.
* If the player's score goes above 21, the player busts and the computer wins.
* If the player chooses **stand**, the computer starts drawing cards.
* The computer continues drawing cards until its score reaches **17 or higher**.
* Finally, the scores of both the player and computer are compared.

### Game Result

After both the player and computer finish drawing cards:

* If the player's score is greater than 21, the player busts and the computer wins.
* If the computer's score is greater than 21, the computer busts and the player wins.
* If neither player busts, the player with the higher score wins.
* If both have the same score, the game ends in a draw.

## Technologies Used

* **Python**
* **Random Module**

## How to Run

1. Open the project in VS Code.
2. Open the terminal.
3. Run:

```bash
python blackjack-game.py
```

4. Follow the instructions shown in the terminal.

## Features

* Random card generation
* Hit or Stand option
* Automatic computer gameplay
* Ace value adjustment
* Bust detection
* Winner determination
* Draw detection
