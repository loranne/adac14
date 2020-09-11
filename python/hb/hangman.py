print("Hello, world!")
print()

###########################

# HANGMAN GAME

# define a function to take user input of a single letter
# compare it to letters in the word
# if the letter is right, tell user and increment the letter to compare to
# if wrong, guess again
# so I think I'll need a loop within a loop, overall loop is getting the user input
# inner loop is if wrong, guess again... maybe?
# will need another function to determine if user has won
# another function for if user loses? what does loss look like here, without
## the diagram?
# one function to pick a secret word for the user to guess against
# main function will call main loop

# VARIABLES TO TRACK
## user inputs (letters guessed), and whethe right or wrong (dictionary)
## secret answer word (string)
## whether user guessed right or wrong (boolean)
## how many wrong guesses? (integer?)
## NOTE: Why do we need to track the current guess separately??

def handle_input(guess, guessed, answer):
	"""Takes and stores user input of a single letter"""

	# Prompts user for input, converts to lowercase
	# guess = input("Please guess a letter. > ")
	# guess = guess.lower()

	# if the letter has already been guessed, increase guess count
	# if not, add to dictionary guessed
	if guess in guessed:
		guessed[guess] += 1
	
	else:
		guessed[guess] = 1

	# inform user if guess is right or wrong
	if guess in answer:
		print("Right!")
		print()
	
	else:
		print("Wrong!")
		print()
	
	# no return. why?

# loop over each key in guessed to see if it appears in answer
# if yes, print that letter in answer. if no, print a "-" instead
# variable called "progress" will store answer with blanks for letters that haven't been guessed
def show_word(answer, guessed):
	"""Show current progress toward answer"""

	progress = ""

	for letter in answer:
		if letter not in guessed:
			progress = progress + "-"
		
		else: 
			progress = progress + letter
	
	progress = progress.upper()
	
	print(progress)
	print()

# function to determine if user has won
def has_won(answer, guessed):
	"""Checks all guesses against answer to determine if won. Returns true (won) or false (not won)"""

	# loops through each letter in the answer. if it's not in the guessed dictionary, user hasn't won, loop breaks immediately
	for letter in answer:
		if letter not in guessed:
			return False
	
	# this only runs if the loop completes & wasn't broken, meaning user won
	return True

def game_loop(answer):
	"""Main loop for running the hangman game"""

	# need to take user input and store it
	# then call handle_input
	# then call show_word
	# then call has_won
	# if has_won is true, loop breaks
	guessed = {}

	while not has_won(answer, guessed):
		guess = input("Please guess a letter. > ")
		guess = guess.lower()

		handle_input(guess, guessed, answer)
		show_word(answer, guessed)
	
	has_won(answer, guessed)


print("""
          )
         (.)
         .|.
         l7J
         | |
     _.--| |--._
  .-';  ;`-'& ; `&.
 & &  ;  &   ; ;   }}
 {{      ;    &   &_/
  F'''---...---'''J
  | | | | | | | | |
  J | | | | | | | F
   `---.|.|.|.---'

""")
print()

answer = "pie"
print("Let's play!")
print()
game_loop(answer)
print("***YOU WON!***")


##############

# PROBLEMS YET TO FIX

# I notice that this game can technically accept multi-character input. There's no validating for just one character. 
# If I enter "pi" or "ie", for example, it stil evaluates this as a correct answer, and returns "Right!"
# but does not reflect that I've won or reveal the letters guessed. 
