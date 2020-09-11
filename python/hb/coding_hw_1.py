# 1. Function prints congrats and smiley

def congrats():
  print("Congratulations!")
  print(":)")

congrats()
print()

# 2. While loop counts to 5

import time

count = 1

while count < 6:
  print(count)
  time.sleep(1)
  count = count + 1

print()

# 3. Function asks user name and greeting.

def hi_there():
  print("What's your name?")
  name = input("> ")
  name = name.title()
  print("Hi, {}. It's nice to meet you." .format(name))

hi_there()
print()

# 4. While loop asking for number

num_user = 0

while True: 
  num_user = input("Please enter a number between 50 and 100. > ")
  num_user = int(num_user)

  if num_user > 100:
    print("Too high!")
  
  elif num_user < 50:
    print("Too low!")

  elif num_user in range(50, 100):
    break

print()
