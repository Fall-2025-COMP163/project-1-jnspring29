# COMP 163 - Project 1: Character Creator & Saving/Loading

# Name: Jessica Springer

# Date: 10/27/2025

import os

# --- Calculated Stats Function ---

def calculate_stats(character_class, level):
"""
Calculate character stats based on class and level.
Returns a tuple: (strength, magic, health)
"""
character_class_lower = character_class.lower()

```
# Base stats
strength = 5
magic = 5
health = 50

# Adjust stats per class
if character_class_lower == "warrior":
    strength += 90
    magic += 20
    health += 45
elif character_class_lower == "mage":
    strength += 15
    magic += 90
    health += 30
elif character_class_lower == "cleric":
    strength += 35
    magic += 100
    health += 85
elif character_class_lower == "rogue":
    strength += 45
    magic += 35
    health += 25
else:
    # Invalid class returns base stats
    return (strength, magic, health)

# Increase stats per level
strength += level * 5
magic += level * 5
health += level * 10

return (strength, magic, health)
```

# --- Character Creation ---

def create_character(name, character_class):
"""
Create a new character dictionary with stats, gold, and equipment.
Returns None if class is invalid.
"""
valid_classes = ["Warrior", "Mage", "Cleric", "Rogue"]
if character_class not in valid_classes:
return None

```
level = 1
strength, magic, health = calculate_stats(character_class, level)

# Gold assignment
gold_values = {
    "Warrior": 200,
    "Mage": 170,
    "Cleric": 140,
    "Rogue": 110
}
gold = gold_values.get(character_class, 50)

# Starting equipment
equipment_values = {
    "Warrior": ["Steel Sword", "Aluminum Shield", "Iron Armor"],
    "Mage": ["Magic Staff", "Spellbook", "Magic Robe"],
    "Cleric": ["Steel Mace", "Holy Symbol", "Chainmail"],
    "Rogue": ["Steel Dagger", "Lockpick Set", "Leather Armor"]
}
equipment = equipment_values.get(character_class, ["Stick", "Cloth Tunic"])

# Build character dictionary
character = {
    "name": name,
    "class": character_class,
    "level": level,
    "strength": strength,
    "magic": magic,
    "health": health,
    "gold": gold,
    "equipment": equipment
}

return character
```

# --- Display Character ---

def display_character(character):
print("\n=== CHARACTER SHEET ===")
print(f"Name: {character.get('name', '')}")
print(f"Class: {character.get('class', '')}")
print(f"Level: {character.get('level', 0)}")
print(f"Strength: {character.get('strength', 0)}")
print(f"Magic: {character.get('magic', 0)}")
print(f"Health: {character.get('health', 0)}")
print(f"Gold: {character.get('gold', 0)}")
print(f"Equipment: {', '.join(character.get('equipment', []))}")

# --- Level Up Function ---

def level_up(character):
character["level"] += 1
strength, magic, health = calculate_stats(character["class"], character["level"])
character["strength"] = strength
character["magic"] = magic
character["health"] = health
print(f"\n{character['name']} has leveled up to level {character['level']}! Congratulations!")

# --- Save Character to File ---

def save_character(character, filename):
if not isinstance(character, dict) or not filename:
return False

```
directory = os.path.dirname(filename)
if directory and not os.path.exists(directory):
    os.makedirs(directory)

try:
    with open(filename, "w") as file:
        for key, value in character.items():
            if isinstance(value, list):
                value_str = ", ".join(value)
                file.write(f"{key}: {value_str}\n")
            else:
                file.write(f"{key}: {value}\n")
    return True
except:
    return False
```

# --- Load Character from File ---

def load_character(filename):
if not os.path.exists(filename):
return None

```
character = {}
with open(filename, "r") as file:
    lines = file.readlines()
    for line in lines:
        if ": " not in line:
            continue
        key, value = line.strip().split(": ", 1)
        key = key.lower()
        if value.isdigit():
            value = int(value)
        elif ", " in value:
            value = value.split(", ")
        character[key] = value

if len(character) == 0:
    return None
return character
```

# --- Main Program ---

if **name** == "**main**":
print("=== WELCOME TO CHARACTER CREATOR ===")

```
name = input("Enter your character's name: ").strip()

while True:
    character_class = input("Choose a class (Warrior/Mage/Cleric/Rogue): ").strip()
    if character_class in ["Warrior", "Mage", "Cleric", "Rogue"]:
        break
    print("Invalid class! Please choose from Warrior, Mage, Cleric, or Rogue.")

char = create_character(name, character_class)

display_character(char)

# Level up example
level_up(char)
display_character(char)

# Save and load example
save_character(char, "my_character.txt")
loaded_char = load_character("my_character.txt")
print("\nLoaded character from file:")
display_character(loaded_char)
```
