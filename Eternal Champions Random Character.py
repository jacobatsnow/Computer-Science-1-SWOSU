import random
import time

class Character:
    def __init__(self, name, job):
        self.name = name
        self.job = job
    def __str__(self):
        return f"{self.name} - {self.job}"
characters = [
    Character("Shadow", "Assassin"),
    Character("RAX", "Cyborg Boxer"),
    Character("Blade", "Bounty Hunter"),
    Character("Jetta", "Russian Aristocrat and Circus Performer"),
    Character("Slash", "Caveman"),
    Character("Trident", "Atlantean Gladiator"),
    Character("Xavier", "Alchemist"),
    Character("Midknight", "Vampire Biochemist"),
    Character("Larcen", "Cat Burglar")
]

def select_random_character(characters):
    return random.choice(characters)

def typewriter(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

select_random_character
selected = select_random_character(characters)

print("ETERNAL CHAMPIONS RANDOM CHARACTER SELECT")
input("press enter to continue" \
"")
typewriter(str(selected))
