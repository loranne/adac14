print("Hello, World!")
print()

#############################

# Master list of all books in library
books = ["Dune", "Pride and Prejudice"]

# Welcome message
print("Brighticorn's Books")
print("--------------------")
print()

##########################

# Starts loop. Shows user action options.
while True:
  print("You can: (A)DD / (V)IEW / (C)HECK / E(X)IT")

  # User input prompt. Convert input to uppercase. After I got further into the exercise, I noticed that instructions have us going with fully typed user commands and using lowercase. I hope it's okay that I did the exercise this way instead. I get the concept, and wanted to tidy up my project a little more.
  command = input("Action > ")
  command = command.upper()

  # conditionals for variety of possible user input.
  if command == "A":
    command = "Add"
    print("Add Book")
    print()

    # Code for adding book. Prompts user to enter book. Converts user input to title case, and appends title to books list.
    new_book = input("Title > ")
    new_book = new_book.title()
    books.append(new_book)
    print("Added: ", new_book)
    print()

  elif command == "V":
    command = "View"
    print("View Books")
    print()

    # prints all items in list books
    for book in books:
      print(book)
    
    print("***End of list***")
    print()

  elif command == "C":
    command = "Check"
    print("Check Library")
    print()

    # Prompts user to enter title they're checking for. Converts to title case.
    to_check = input("Title >")
    to_check = to_check.title()

    # looks for title user entered in books list. If it's there, returns positive message. 
    if to_check in books:
      print("You already have", to_check)
      print()

    # if it's not, negative message.
    else:
      print("You don't have that book.")
      print()

  # exit command should end the loop, hence break.
  elif command == "X":
    command = "Exit"
    print("Goodbye!")
    print()
    break

  # Accounting for potential invalid user input.
  else:
    print("Sorry, that's not an option.")
    print()
