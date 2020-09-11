print("Hello, world!")

# Intro to game 
print("Are you ready for a Mars adventure?")
print("Booting up...")
print("...")
print("...")
print("...")
print("Ready.")
print()

# Get user's name
name = input("Hi there. We hear you want to head to Mars. What's your name? > ")
name = name.title()

# Explains game
print()
print("Hi,", name, "---Welcome to Mars (or to your Mars adventure, anyway.")
print("Yesterday, you received a call from your good friend at NASA.")
print("They need someone to go to Mars this weekend for a sepcial mission, and they're hoping you can help them out.")
print()

# Ask user if excited to go to Mars
print("Are you excited about your mission? Type 'Y' or 'N'.")
excited = input("> ")
excited = excited.upper()

if excited == "Y":
  print("I knew it! It's so cool that you're going to Mars!!!")

else: 
  print("Well, you should have thought of that before you acceepted this mission. Too late to back out now!")
print()

# Packing for Mars (hi, Mary Roach)

print()
print("Let's get packed for your trip to Mars.")

# Suitcases
print("How many suitcases do you want to take with you?")
num_suitcases = input("> ")
num_suitcases = int(num_suitcases)

if num_suitcases > 2:
  print("That's a lot of luggage! It's a pretty cramped shuttle. You'll have to leave something behind. Please try to fit your stuff into 2 suitcases.")

else: 
  print("Perfect! Your luggage will fit in the shuttle.")

# Companion

print()
print("You're allowed to bring one companion animal with you.")

print("What kind of companion animal would you like to bring?")
companion_type = input("> ")
companion_type = companion_type.lower()

print("What is your companion's name?")
companion_name = input("> ")
companion_name = companion_name.title()

# Confirm companion 
print("Great, so you're bringing", companion_name, "the", companion_type, end=".\n")

# Spaceship decor

print()
print("NASA has an interior design team offering to outfit your shuttle.")
print("You have a few options for the interior decor of the shuttle.")
print()
print("Your options are:")
print("A) Sleek, modern minimalism")
print("B) Retro/vintage space age")
print("C) SF hippie chic")

print()
print("What type of decor would you prefer? Choose A, B, or C.")
decor_type = input("> ")
decor_type = decor_type.upper()

if decor_type == "A":
  decor = "modern minimalist"

elif decor_type == "B":
  decor = "retro"

elif decor_type == "C":
  decor = "hippie chic"

else:
  decor = "unfinished basement"

# Big finish

print()
print("I can see it now...")
print(name, "and", companion_name, "surfing the celestial abyss...")
print("in a", decor, "shuttle.")

# Liftoff

import time

timer = 5

while timer > 0:
  print(timer, "...")
  time.sleep(5)
  timer = timer - 1

print("*** LIFTOFF ***")
