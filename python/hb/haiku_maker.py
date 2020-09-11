# PSEUDOCODE
# 1 Loop starts
# 2 Ask user for input
# 3 If/else statement
# 3.1 If user input is "Sad" x happens. 
# 3.2 If user input is "silly" y happens.
# 4 Prompt for another haiku
# 5 Another if/else statement
# 5.1 If user input is y, loop restarts
# 5.2 If user input is n, break. 
# We'll need a library of words and some way of demarcating syllables, as well as choosing words that are sad vs. silly.

# imports random library
import random

# 1st function: haiku structure
def design_haiku(num_lines, first_lines, middle_lines, final_lines):
  """Print three randomly chosen lines to form haiku"""
  
  # selects random lines from appropriate lists
  first_line = random.choice(first_lines)
  middle_line = random.choice(middle_lines)
  final_line = random.choice(final_lines)

  # The way I've written my if statements here has 
  # created line spacing issues. i.e. there's an extra # blank line between lines 1 and 2, but not 2 and 3.
  print()
  print("Your free-range, machine-crafted haiku is...")
  print()
  print(first_line)
  
  if num_lines >= 2:
    print(middle_line)

  if num_lines == 3:
    print(final_line)
  
  print()

# 2nd function, lets user pick haiku style
def choose_haiku_style():
  """Choose haiku style, ensure user picks valid style"""
  
  # Gives user options for haiku type
  print("Would you like a silly, sad, or nature haiku?")

  # Loop to prompt user for and validate input
  while True:

    # variable containing list of choice options  
    style_choices = ["silly", "sad", "nature"]

    # gets user input and formats to lowercase  
    style = input("Enter 'silly', 'sad' or 'nature'. > ")
    style = style.lower()

    # validates user input 
    if style in style_choices:
      return style
    
    else: 
      print("I'm sorry, that's not a valid haiku theme.")
  
  print()

# 3rd function: how many lines?
def get_num_lines():
  """Prompts user for number of lines in haiku"""

  while True:
    num_lines = input("How many lines would you like your haiku to be? > ")
    num_lines = int(num_lines)

    if num_lines not in range(1, 4):
      print("Please choose a number between 1 and 3.")
    
    else:
      return num_lines

def get_lines(filename):
  """Get poem lines based on a file name"""

  # opens file, defines variable that is list "lines"
  f = open(filename)
  lines = []

  # adds each subsequent line to list
  for line in f:
    line = line.strip()
    lines.append(line)
  
  return lines

# 4th overall function (will call preceding
# functions): playing the haiku game
def make_haiku():

  # loop to generate haiku
  while True:

    # calls function to choose haiku style and get
    # user input
    style = choose_haiku_style()
    print()
    num_lines = get_num_lines()
    print()

    # sets conditions for which files to pull from 
    # (silly, sad, or nature)
    if style == "silly":
      silly_first = get_lines("silly_first_lines.txt")
      silly_middle = get_lines("silly_middle_lines.txt")
      silly_final = get_lines("silly_final_lines.txt")

      design_haiku(num_lines, silly_first, silly_middle, silly_final)

    if style == "sad":
      sad_first = get_lines("sad_first_lines.txt")
      sad_middle = get_lines("sad_middle_lines.txt")
      sad_final = get_lines("sad_final_lines.txt")

      design_haiku(num_lines, sad_first, sad_middle,    sad_final)
    
    if style == "nature":
      nature_first = get_lines("nature_first_lines.txt")
      nature_middle = get_lines("nature_middle_lines.txt")
      nature_final = get_lines("nature_final_lines.txt")
      
      design_haiku(num_lines, nature_first, nature_middle, nature_final)
    
    # does user want more haiku? breaks if not
    play_again = input("Would you like another haiku? > ")
    play_again = play_again.lower()

    if play_again.startswith("n"):
      print("Goodbye!")
      break

    print()

# calls the final function
make_haiku()
