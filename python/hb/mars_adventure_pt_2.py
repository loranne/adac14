# Tell user what program is going to do 
print("Record your observations.")

# Start loop. Prompt for user input.
while True: 
  print()
  print("What do you see?")
  observation = input("> ")

  # Break loop if user hits return without entering observation.
  if observation == "":
    break

  # Check if observation string ends with a period. Appends period if not.
  if not (observation.endswith(".")):
    observation = observation + "."

    # Appends "Noted:" to observation recorded.
    print('Noted: "' + observation + '"')

print()
print("Finished with observations.")

print()

#######################################

# Defines variables for correct door code and number of wrong guesses.
door_code = "8888"
wrong_count = 0

# Starts loop
while True:
  # Promts user for door code.
  print("Please enter the door code.")
  code_guess = input("> ")

  # Key logic of the loop: isdigit checks that use input is digits only AND that the length of that string is 4 characters.
  if code_guess.isdigit() and len(code_guess) == 4:

    # If they get it right, the door opens and the loop ends.  
    if code_guess == door_code:
      print ("Door code: ", code_guess)
      print("Open the door!")
      break
  
    # If they get it wrong, adds +1 to the count of wrong guesses.
    else: 
      wrong_count = wrong_count + 1
      print ("Door code: ", code_guess)
      print("Wrong guesses: ", wrong_count)

  # If the user entered a string that is NOT digits only OR that is not 4 characters in length, prints invalid message. Adds + 1 to wrong guesses count.
  else:
    wrong_count = wrong_count + 1
    print("Invalid entry!")
    print("Wrong guesses: ", wrong_count)

print()

#######################################

# Imports the random library
import random

# Defines a variable "hits" for the number of times a shot hits Darth COBOL. List "result" is a list of all possible outcomes of each shot (hit or miss)
hits = 0 
result = ['hit', 'miss']

# Starts loop.
while True:
# 50/50 chance of a hit, so the result of one shot is going to be chosen at random from "result" list. I'm not 100% clear on my formatting of the lines below. I feel like they should be broken up a bit more, but I'm not sure how.
  fight = input("Press ENTER to fire.")
  shoot = random.choice(result)
  print("You {}!" .format(shoot))
    
  # Counts number of hits only
  if shoot == 'hit':
    hits = hits + 1
  
  # When you've hit 3x, you win the duel and loop breaks.
  if hits == 3:
    print("You have defeated Darth COBOL!")
    break

print()

#######################################

# Imports time library
import time

# Defintes variable count
countdowns = 0

# Starts greater loop, where we add to the number of countdowns each time. We only want it to countdown thrice.
while countdowns < 3:
  countdowns = countdowns + 1
  
  # Variable "timer" is defined here because we need it to restart at 5 on each pass through the loop.
  timer = 5

  # This block is pulled exactly from previous lab.
  while timer > 0:
      print(timer, "...")
      time.sleep(2)
      timer = timer - 1

# Liftoff is outside the loop, because we only want to print it once.
print("*** LIFTOFF ***")
