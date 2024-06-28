# Text-Based Adventure Game

## Overview
This is a simple text-based adventure game written in Python. Players can create a character, make decisions that affect the storyline, manage an inventory, and solve puzzles to complete quests. The game is designed to be modular for easy updates and expansions.

## Features
- **Character Creation**: Choose your character's name, race (Human, Elf, Dwarf), and profession (Warrior, Mage, Thief).
- **Decision Making & Branching Story Paths**: Make choices that lead to different story outcomes.
- **Inventory Management**: Add and remove items from your inventory.
- **Puzzles and Quests**: Solve puzzles to complete quests and progress in the game.
- **Modular Code Structure**: Easy to update and expand.

## Getting Started

### Prerequisites
- Python 3.x

### Installation
1. Clone the repository or download the script.
   ```bash
   git clone https://github.com/yourusername/text-adventure-game.git
   cd text-adventure-game
   ```

### Running the Game
1. Navigate to the directory containing the script.
2. Run the script using Python.
   ```bash
   python game.py
   ```

## How to Play
1. Follow the prompts to create your character by entering a name, race, and profession.
2. Make decisions to progress through the story by choosing from given options.
3. Manage your inventory by adding or removing items using the inventory command.
4. Solve puzzles to complete quests and advance the story.

## Commands
- `story`: Progress through the story based on your decisions.
- `inventory`: Manage your inventory by adding or removing items.
- `quit`: Exit the game.

## Code Structure

### Character Class
Handles character creation and stores character attributes such as name, race, profession, inventory, and health.

### Game Class
Manages the main game loop, including character creation, decision making, inventory management, and story progression.

### Puzzle Class
Represents a puzzle with a question and an answer. Used to create and manage puzzles in quests.

### Quest Class
Represents a quest containing a description and a series of puzzles. Manages quest progression and completion.

## Example Usage
1. Run the game:
   ```bash
   python game.py
   ```
2. Follow the prompts to create your character:
   ```plaintext
   Enter your character's name: Aragorn
   Choose your race (Human, Elf, Dwarf): Human
   Choose your profession (Warrior, Mage, Thief): Warrior
   ```
3. Make choices to progress through the story:
   ```plaintext
   You find yourself at the entrance of a dark forest. Do you:
   1. Enter the forest
   2. Walk along the edge of the forest
   > 1
   ```
4. Manage your inventory:
   ```plaintext
   Enter a command (story, inventory, quit): inventory
   Current Inventory: ['Mysterious Artifact']
   Do you want to (1) Add or (2) Remove an item? 1
   Enter the item to add: Sword
   Updated Inventory: ['Mysterious Artifact', 'Sword']
   ```

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact
If you have any questions or feedback, feel free to reach out to [mohammadsaalimiraqi@gmail.com].

---

Enjoy the game and happy adventuring!
