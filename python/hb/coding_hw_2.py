# CONDITOINALS ###############
# 1 #############
sentence = "Time flies when you're coding."

if len(sentence) > 15:
  print("Longer than 15 characters.")

else:
  print("Not longer than 15 characters")

print()

# 2 ##############
print("Welcome to the adder-subtractulator!")

num1 = input("What is number 1? ")
num1 = int(num1)

num2 = input("What is number 2? ")
num2 = int(num2)

# starts loop, necessary in event of invalid input
while True: 
  print("Would you like to add or subtract those numbers?")
  print("Please type + or -")

  operator = input("> ")

  # conditional for adding numbers
  if operator == "+":
    result = num1 + num2
    print("The result is", result)
    break

  # conditional for subtracting numbers
  elif operator == "-":
    result = num1 - num2
    print("The result is", result)
    break

  else: 
    print("Sorry, can only add or subtract.")

print()

# 3 #########################

croissant_1 = ["Yao", 4, "golden brown", "crescent"]
croissant_2 = ["Alana", 33, "golden brown", "crescent"]
croissant_3 = ["George", 27, "golden brown", "crescent"]
croissant_4 = ["George", 27, "light brown", "crescent"]

# else/if statements for croissant_1
if croissant_1[1] >= 6 and croissant_1[3] == "crescent"   and croissant_1[2] == "golden brown":
  print("{} can enter the competition.".format(croissant_1[0]))

else:
  print("{} cannot enter the competition.".format(croissant_1[0]))

if croissant_2[1] >= 6 and croissant_2[3] == "crescent" and croissant_2[2] == "golden brown":
  print("{} can enter the competition.".format(croissant_2[0]))

else:
  print("{} cannot enter the competition.".format(croissant_2[0]))

if croissant_3[1] >= 6 and croissant_3[3] == "crescent" and croissant_3[2] == "golden brown":
  print("{} can enter the competition.".format(croissant_3[0]))

else:
  print("{} cannot enter the competition.".format(croissant_3[0]))

if croissant_4[1] >= 6 and croissant_4[3] == "crescent" and croissant_4[2] == "golden brown":
  print("{} can enter the competition.".format(croissant_4[0]))

else:
  print("{} cannot enter the competition.".format(croissant_4[0]))

# LOOPS ######################
# 1 ####################

students = ["Julia", "Sarah", "Andy", "Charlotte", "Taylor", "Sam"]

for student in students:
  print(student)

i = 0

while i < len(students):
  print(i)
  i = i + 1

students.sort()

for student in students:
  print(student)
