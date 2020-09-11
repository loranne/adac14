# define a function to count to 3
def count_to_three():
  
  # Set number at 1
  count = 1

  # start loop, print each number in range
  while count < 4:
    for count in range(1, 4):
      print(count)
      count = count + 1

# call function
count_to_three()
print()

###############################

def greater_than_ten(integers):
  """Function to find integers greater than 10"""

  big_int = []

  for num in integers:
    if num > 10:
      big_int.append(num)
  
  return big_int

integers = [1, 5, 23, 89, 11, 84, 5]

big_integers = greater_than_ten(integers)
print(big_integers)
print()

################################

def make_sentence(person, place):
  """Function returns sentence, like a mad lib, using arguments"""

  return "Today I saw {} doing cartwheels in {}.".format(person, place)

# saves return value as variable sentence
sentence = make_sentence("Captain Kirk", "Paris")
print(sentence)
print()

###################################

def find_words_in_common(list1, list2):
  """Takes in 2 lists of words, returns new list of words in both lists"""

  both_list = []

  # evaluates each item in list1, checks to see if it's 
  # in list 2. If in list 2, adds to new list
  for word in list1:
    if word in list2:
      both_list.append(word)
  
  return both_list

# 2 lists of words
hello_list = ["hello", "aloha", "hola", "bonjour", "ahlan"]

goodbye_list = ["goodbye", "aloha", "adios", "adieu", "ma' salama"]

# call function, and print return value
new_list = find_words_in_common(hello_list, goodbye_list)
print(new_list)
print()

######################################

def sum_unique_nums(nums_list):
  """Finds unique integers in list, adds them together"""

  # blank list for populating with unique numbers
  unique_nums = []

  # evaluate each item in list. if not in new list 
  # already, add it
  for num in nums_list:
    if num not in unique_nums:
      unique_nums.append(num)
  
  # adds together numbers in new list
  total = sum(unique_nums)

  return total

# list of numbers to evaluate
my_nums = [4, 8, 4, 2, 15, 9, 1, 11, 8]

# call function and save return
sum_all = sum_unique_nums(my_nums)
print(sum_all)
print()

#####################################

def select_evenly_divisible_integers(num1, num2, num3):
  """Function to return list of integers that are evenly divisible by at least one number in arguments"""

  # blank list to be populated with evenly divisible 
  # integers
  evenly_divided_nums = []

  # evaluates each integer in range 1 - 100 inclusive, # dividing each one in turn by each of the three
  # integers in arguments
  for num in range(1, 101): 
    if num % num1 == 0 or num % num2 == 0 or num % num3 == 0:
      evenly_divided_nums.append(num)
  
  # returns new list of evenly divisible numbers
  return evenly_divided_nums

# save return value as variable and print return
new_nums = select_evenly_divisible_integers(10, 12, 25)
print(new_nums)
print()
