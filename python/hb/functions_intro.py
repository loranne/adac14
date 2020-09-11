print("Hello World!")
print()

import random

# PART 1 ######################

# Defines function hello_print
def hello_print():
  print("Hello")

# Calls function hello_print
hello_print()
print()

# defines fucntion hello_return
def hello_return():
  return "hello"

# assigns variable greet to return of function hello_return
greet = hello_return()
print(greet)
# calls function hello_return
hello_return()
print()

# PART 2 #####################

"""Generates a lucky number"""

# The line below allows us to use the function randint 
from random import randint

def prints_random_number():
  """Prints a random number"""

  # randint returns a random integer, we're giving it 0 and 10, so it'll return
  # a random integer between 0 - 10
  # for more info: https://docs.python.org/2/library/random.html#random_randint

  print(randint(0, 10))

prints_random_number()
print()
# PART 3 #######################

def add(num1, num2):
  """Returns sum of two numbers"""

  # sum is a built-in function in python, so can't use it as a variable name 
  summation = num1 + num2

  return summation

######################################
# Complete all functions below

def subtract(num1, num2):
  """Returns result of one number subtracted from the other"""

  minus = num1 - num2

  return minus

def multiply(num1, num2):
  """Returns result of two numbers multiplied"""

  product = num1 * num2 

  return product

def divide(num1, num2):
  """Returns result of one number divided by the other"""

  quotient = num1 // num2 

  return quotient

def modulo(num1, num2):
  """Returns what would be the remainder of a division operation between two numbers"""

  remainder = num1 % num2

  return remainder 

def power(base, exponent):
  """Returns the the result of an exponential equation"""

  power_of = base ** exponent
  
  return power_of

def square(num1):
  """Returns a number squared"""

  num_squared = num1 ** 2

  return num_squared
  
result_1 = add(3, 14)
print(result_1)

result_2 = subtract(49, 30)
print(result_2)

result_3 = multiply(3, 4)
print(result_3)

result_4 = divide(15, 5)
print(result_4)

result_5 = modulo(12, 5)
print(result_5)

result_6 = power(2, 5)
print(result_6)

result_7 = square(4)
print(result_7)
