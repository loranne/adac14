print("Hello, world!")
print()

##############################

# PART 2

employees = [('Jane', 1),
             ('Sally', 2),
             ('Bill', 3),
             ('Bob', 4),
             ('Brian', 5),
             ('Julie', 6),
             ('Jorge', 7),
             ('Chelsea', 8),
             ('Sandra', 9),
             ('Rudy', 10),
             ('Ralph', 11)]

def print_employee_numbers():
  """Print each employee name and hiring order"""
  
  # Loops through each tuple
  for employee in employees:

    # defines tuple indices as specific pieces of data 
    # pertaining to each employee record
    name = employee[0]
    hiring_order = employee[1]

    print("{} was employee number {}.".format(name, hiring_order))

print_employee_numbers()
print()

#############################

# PART 3

animal_counts = {'goat': 4, 'horse': 2, 'turtle': 6,  'duck': 1}

# Function to add one individual animal to a dicitonary
# of animals
def add_animal(new_animal_name, animals):
  """Adds a new animal to our animal_counts dictionary"""

  # changes animal name to lowercase, so adding "Horse"
  # and "horse" should have the same result
  new_animal_name = new_animal_name.lower()

  # checks if animal name is already in animals if it 
  # is, +1
  if new_animal_name in animals:
    animals[new_animal_name] += 1

  # if not, it's value is set at 1
  else:
    animals[new_animal_name] = 1

  return animals

# discovered that if I change this one to "Horse", adds # a whole new entry. not ideal! 
new_animal_counts = add_animal("Horse", animal_counts)
new_animal_counts = add_animal("goose", animal_counts)
new_animal_counts = add_animal("chinchilla", animal_counts)
print(new_animal_counts)
print()
