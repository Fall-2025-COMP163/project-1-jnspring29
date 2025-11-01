# project1_starter.py

# COMP 163 - Project 1: Character Creator & Chronicles

# Name: Jessica Springer

# Date: 10/27/2025

# AI Usage: Assisted in debugging and ensuring autograder compatibility

import os

# --- Calculate Stats ---

def calculate_stats(character_class, level):
"""
Returns a tuple (strength, magic, health) based on class and level.
"""
base_stats = {
"Warrior": (95, 35, 125),
"Mage": (20, 95, 80),
"Rogue": (50, 50, 60),
"Cleric": (40, 90, 120)
}
if character_class not in base_stats:
return (0, 0, 0)

```
strength, magic, health = base_stats[character_class]

# Level scaling
strength += 5 * (level - 1)
magic += 5 * (level - 1)
health += 10 * (level - 1)

return (strength, magic, health)
```

# --- Create Character ---

def create_character(name, character_class):
"""
Returns a character dictionary with required stats.
Returns None if class is invalid.
"""
valid_classes = ["Warrior", "Mage", "Rogue", "Cleric"]
if character_class not in valid_classes:
return None

```
level = 1
strength, magic, health = calculate_stats(character_class, level)

gold_values = {"Warrior": 200, "Mage": 170, "Rogue": 110, "Cleric": 140}
gold = gold_values[character_class]

return {
    "name": name,
    "class": character_class,
    "level": level,
    "strength": strength,
    "magic": magic,
    "health": health,
    "gold": gold
}
```

# --- Display Character ---

def display_character(character):
"""
Prints character info in required format.
"""
print(f"Character Name: {character.get('name','')}")
print(f"Class: {character.get('class','')}")
print(f"Level: {character.get('level',0)}")
print(f"Strength: {character.get('strength',0)}")
print(f"Magic: {character.get('magic',0)}")
print(f"Health: {character.get('health',0)}")
print(f"Gold: {character.get('gold',0)}")

# --- Level Up ---

def level_up(character):
"""
Increase character level by 1 and recalculate stats.
"""
character["level"] += 1
s, m, h = calculate_stats(character["class"], character["level"])
character["strength"] = s
character["magic"] = m
character["health"] = h

# --- Save Character ---

def save_character(character, filename):
"""
Save character to file in exact required format.
Returns True on success, False on failure.
"""
if not isinstance(character, dict) or not filename:
return False
directory = os.path.dirname(filename)
if directory and not os.path.exists(directory):
os.makedirs(directory)
try:
with open(filename, "w") as f:
f.write(f"Character Name: {character['name']}\n")
f.write(f"Class: {character['class']}\n")
f.write(f"Level: {character['level']}\n")
f.write(f"Strength: {character['strength']}\n")
f.write(f"Magic: {character['magic']}\n")
f.write(f"Health: {character['health']}\n")
f.write(f"Gold: {character['gold']}\n")
return True
except:
return False

# --- Load Character ---

def load_character(filename):
"""
Load character from file. Returns dict or None if file missing/invalid.
"""
if not os.path.exists(filename):
return None
character = {}
with open(filename, "r") as f:
for line in f:
if ": " not in line:
continue
key, value = line.strip().split(": ", 1)
if key in ["Level","Strength","Magic","Health","Gold"]:
try:
value = int(value)
except:
value = 0
char_key = "name" if key=="Character Name" else key.lower()
character[char_key] = value
return character if character else None

# --- Main Program ---

if **name** == "**main**":
print("=== Character Creator ===")
name = input("Enter character name: ")
while True:
char_class = input("Choose class (Warrior/Mage/Rogue/Cleric): ")
if char_class in ["Warrior","Mage","Rogue","Cleric"]:
break
print("Invalid class! Please choose a valid option.")

```
char = create_character(name, char_class)
print("\nCharacter Sheet:")
display_character(char)

level_up(char)
print("\nAfter Level Up:")
display_character(char)

save_character(char,"my_character.txt")
print("\nLoaded from file:")
loaded = load_character("my_character.txt")
display_character(loaded)
```
