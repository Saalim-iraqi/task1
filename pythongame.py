import sys

# Character creation
class Character:
    def __init__(self, name, race, profession):
        self.name = name
        self.race = race
        self.profession = profession
        self.inventory = []
        self.health = 100

    def __str__(self):
        return f"Name: {self.name}, Race: {self.race}, Profession: {self.profession}, Health: {self.health}, Inventory: {self.inventory}"

# Decision making and branching paths
class Game:
    def __init__(self):
        self.character = None
        self.story_position = 0

    def start(self):
        self.create_character()
        self.story()

    def create_character(self):
        name = input("Enter your character's name: ")
        race = input("Choose your race (Human, Elf, Dwarf): ")
        profession = input("Choose your profession (Warrior, Mage, Thief): ")
        self.character = Character(name, race, profession)
        print(f"Character created: {self.character}")

    def story(self):
        if self.story_position == 0:
            self.story_position += 1
            print("You find yourself at the entrance of a dark forest. Do you:")
            print("1. Enter the forest")
            print("2. Walk along the edge of the forest")
            choice = input("> ")
            if choice == '1':
                self.enter_forest()
            elif choice == '2':
                self.walk_edge()
            else:
                print("Invalid choice. Try again.")
                self.story()
        elif self.story_position == 1:
            # Continue story from different path
            pass

    def enter_forest(self):
        print("You enter the forest and find a mysterious artifact.")
        self.character.inventory.append("Mysterious Artifact")
        self.story_position += 1
        self.story()

    def walk_edge(self):
        print("You walk along the edge and find a hidden path.")
        self.story_position += 1
        self.story()

# Inventory management
    def manage_inventory(self):
        print(f"Current Inventory: {self.character.inventory}")
        action = input("Do you want to (1) Add or (2) Remove an item? ")
        if action == '1':
            item = input("Enter the item to add: ")
            self.character.inventory.append(item)
        elif action == '2':
            item = input("Enter the item to remove: ")
            if item in self.character.inventory:
                self.character.inventory.remove(item)
            else:
                print("Item not found in inventory.")
        else:
            print("Invalid action.")
        print(f"Updated Inventory: {self.character.inventory}")

    def run(self):
        while True:
            command = input("Enter a command (story, inventory, quit): ")
            if command == "story":
                self.story()
            elif command == "inventory":
                self.manage_inventory()
            elif command == "quit":
                print("Exiting game.")
                sys.exit()
            else:
                print("Unknown command.")

# Puzzles and quests
class Puzzle:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def ask(self):
        response = input(self.question + " ")
        if response.lower() == self.answer.lower():
            print("Correct!")
            return True
        else:
            print("Incorrect.")
            return False

class Quest:
    def __init__(self, description, puzzles):
        self.description = description
        self.puzzles = puzzles

    def start(self):
        print(self.description)
        for puzzle in self.puzzles:
            if not puzzle.ask():
                print("Quest failed.")
                return
        print("Quest completed!")

def main():
    game = Game()
    game.start()
    puzzle1 = Puzzle("What is 2+2?", "4")
    puzzle2 = Puzzle("What is the capital of France?", "Paris")
    quest = Quest("Solve these puzzles to continue your journey:", [puzzle1, puzzle2])
    quest.start()
    game.run()

if __name__ == "__main__":
    main()
