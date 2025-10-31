#--- Project & Codering information ---
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Jessica Springer
Date: 10/27/2025

AI Usage: [Document any AI assistance used]

#--- Character Classes: ---
#Warrior - High strength, low magic, high health
#Mage - Low strength, high magic, medium health
#Rogue - Medium strength, medium magic, low health
#Cleric - Medium strength, high magic, high health

# Character creation
def create_character(name, character_class):
     
    Creates a new character dictionary with calculated stats based on class
    Loops until a valid class is entered #So user can keep using inputs until they do the right one

    Level = 1
    strength, health, magic = calc_stats(character_class, level)

    valid_classes = ["Warrior", "Mage", "Cleric", "Rogue"]
    if character_class not in valid_classes:
        return None

#Bonus- Gold calculation system
if character_class == "Warrior":
    gold = 200
elif character_class == "Mage":
    gold = 170
elif character_class == "Cleric":
    gold = 140
elif character_class == "Rogue":
    gold = 110
else:
    gold = 50 #basic starting amount

#Bonus- Starting equipment system
#Ai and google was used to come up with the best items for each character
if character_class == "Warrior":
    equipment = ["Steel Sword", "Aluminum Sheild", "Iron Armor"]
elif character_class == "Mage":
    equipment = ["Magic Staff", "Spellbook", "Magic Robe"]
elif character_class == "Cleric":
    equipment = ["Steel Mace", "Holy SheilSymbold", "Chainmail"]
elif character_class == "Rogue":
    equipment = ["Steel Dagger", "Lockpick Set", "Leather Armor"]
else:
    equipment = ["Stick", "Cloth Tunic"] #basic character starter pack
    
#save_character() function formatting
character = {
    "name": name,
    "class": character_class,
    "level": 1,
    "strength": strength,
    "magic":, magic,
    "health": health,
    "gold": gold
}
    
    return character

#Calculated stats and classes

def calculate_stats(character_class, level):
    character_class = character_class.lower()
    strength = 5 #fix sign
    magic = 15
    health = 80
    
    if character_class == "Warrior":
        strength += 90
        magic += 20
        health += 45
    elif character_class == "Mage":
        strength += 15
        magic += 90
        health += 30
    elif character_class == "Cleric"):
        strength += 35
        magic += 100
        health += 85
     elif character_class == "Rogue"):
        strength += 45
        magic += 35
        health += 10
    else:
        print("Invlaid!")
        return calculate_stats("Warrior", level)
    return strength, health, magic
  
   # File formatting and character saving

def save_character(character, filename):
    import os
    if no isinstance(character, dict) or not filename:
    return False
directory = os.path.dirname(filename)
if directory and not os.path.exists(directory):
    return False
    
    with open(filename, "w") as file:
        file.write(f"Character Name: {character['name']}\n")
        file.write(f"Class: {character['class']}\n")
        file.write(f"Level: {character['level']}\n")
        file.write(f"Strength: {character['strength']}\n")
        file.write(f"Magic: {character['magic']}\n")
        file.write(f"Health: {character['health']}\n")
        file.write(f"Gold: {character['gold']}\n")
    return True

#Character loading
import os

def load_character(filename):
    if not os.path.exists(filename):
        return None

    file = open(filename, 'r')
    lines = file.readlines()
    file.close()

character = {}
for line in lines:
    if ": " not in line:
        continue
    key, value = line.strip().split(": ", 1)
    key = key.lower().replace("character ", "")
    if value.isdigit():
        value = int(value)
    character[key] = value

if len(character) == 0:
    return None

#Character display

def display_character(character):
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character.get('name', '')}")
    print(f"Class: {character.get('class', '')}")
    print(f"Level: {character.get('level', 0)}")
    print(f"Strength: {character.get('strength', 0)}")
    print(f"Magic: {character.get('magic', 0)}")
    print(f"Health: {character.get('health', 0)}")
    print(f"Gold: {character.get('gold', 0)}")

#leveling up

def level_up(character):
    character["level"] += 1
    s, h, m = calculate_stats(character["class"], character["level"])
    character["strength"] = s
    character["health"] = h
    character["magic"] = m
    print(f"\n{character['name']} has leveled up to level {character['leve;']}! Congratulations!)

# Function Testing 
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    n = input("Please enter your name: ")
    c = input("Please choose a class (Warrior/Mage/Cleric/Rogue): ")

char = create_character(n, c)
if char is not None:
    disp_character(char)
    level_up(char)
    disp_character(char)
    save_character(char, "my_character.txt")
    loaded = load_character("my_character.txt")
    print("\nloaded character from file:")
    disp_character(loaded)
else:
    print("The class you have chosen is invalid. Please choose from Warrior, Mage, Cleric, or Rogue")
