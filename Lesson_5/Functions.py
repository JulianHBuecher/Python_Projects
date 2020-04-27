# Usage of Functions in Python
from datetime import datetime
# Printing the current date time
# def print_time():
#     print("Task Completed")
#     print(datetime.now())
#     print()

# Printing the current time with a passed argument
def print_time(task_name = None):
    if task_name is None:
        print("Task Completed")
    else:
        print(task_name)
    print(datetime.now())
    print()

first_name = "Susan"
print_time("First Name assigned")

for x in range(0,10):
    print(x)
    print_time()

# Writing a function for getting the name initials
def get_initial(name):
    initial = name[:1].upper()
    return initial

first_name = input("What is your first name: ")
last_name = input("What is your last name: ")

print("Your Initials are: "+get_initial(first_name)+get_initial(last_name))

# Writing a function with multiple arguments
def get_initial_updated(name, force_uppercase=True):
    if force_uppercase:
        initial = name[:1].upper()
    else:
        initial = name[:1].lower()
    return initial

first_name = input("What is your first name: ")
last_name = input("What is your last name: ")

print("Your Initials are: "+get_initial_updated(first_name)+get_initial_updated(last_name))
print("Your Initials are: " + get_initial_updated(force_uppercase=False,name=first_name)  
        + get_initial_updated(force_uppercase=False,name=last_name))
