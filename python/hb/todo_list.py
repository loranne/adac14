print("Hello, World!")
print()

#############################

def start_todo_list():
  """Main function to run the to-do list app."""

  print("Welcome to your To-Do List Manager!")
  print()
  print("Would you like to:")
  print("[A]dd a new task")
  print("[D]elete a task")
  print("[E]dit a task")
  print("[V]iew all tasks")
  print("[Q]uit the program")
  print()

  # Master list of tasks
  todo_list = []

  while True:
    user_option = input("Choose an option: ")
    user_option = user_option.upper()
    
    if user_option == "A":
      new_task = input("New task: ")
      todo_list.append(new_task)
      print("Added ", new_task)
    
    elif user_option == "D":
      for i, task in enumerate(todo_list):
        print("[{}] {}".format(i + 1, task))
      
      # gets user input on which task to delete 
      # converts user input to integer and reverts
      # to actual index num
      delete_task = input("Delete task: ")
      delete_task = int(delete_task) - 1

      todo_list = todo_list.pop(delete_task)
      print("Task deleted.")

    # editing a task
    elif user_option == "E":
      # prints a numbered list of all tasks
      for i, task in enumerate(todo_list):
        print("[{}] {}".format(i + 1, task))
      
      # prompts user for which task to edit.
      edit_task_index = input("Edit task: ")
      edit_task_index = int(edit_task_index) - 1

      # gets edited text for task.
      new_edit_task = input("New task text: ")

      # replaces original task text with edited text
      todo_list[edit_task_index] = new_edit_task

      print("Task edited.")

    # viewing to-do list
    elif user_option == "V":
      #checks todo_list isn't empty of tasks
      if not todo_list:
        print("No tasks!")
      
      else:
        for task in todo_list:
          print(task) 

    elif user_option == "Q":
      print("Goodbye!")
      break
    
    else:
      print("Sorry, that's not an option.")

start_todo_list()
