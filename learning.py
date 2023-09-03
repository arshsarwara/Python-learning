#strings
print("200 is a great number")
# numbers
print(2)
#Boolean
# print(-2>-5)

print("20 days are xxx minites")
print(20*24*60)
#String concatination (f stands for format and only works for python3)
print("20 days are "+ str(50) + " minutes")
print(f"20 days are {50} minutes")

# Variables
calculation_to_units = 24 * 60 * 60 # no need to specify the datatype, python automatically picks the data type unlike other languages
name_of_unit = "seconds"
print(f"20 days are {20 * calculation_to_units} {name_of_unit}")
print(f"20 days are {35 * calculation_to_units} {name_of_unit}")
print(f"20 days are {50 * calculation_to_units} {name_of_unit}")
print(f"20 days are {110 * calculation_to_units} {name_of_unit}")
# be careful abour reserved words, cannot be used as vars

# functions (define function)"block of code that does something to avoid using the repeating logic"
# when defining function it expects 2 blank line before function
calculation_to_units = 24 * 60 * 60 # no need to specify the datatype, python automatically picks the data type unlike other languages
name_of_unit = "seconds"


def days_to_units(num_of_days, custome_message):
    print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}")
    print(custome_message)


days_to_units(20, "Awsome!")  # calling the function
days_to_units(35, "Looks Good!")

# Scope  (A variable is only available form inside the region it is created)

def scope_check(num_of_days):
    my_var = "variable inside functions"
    print(name_of_unit)
    print(num_of_days)
    print(my_var)
scope_check(20) # error if num_of_days not defined inside

# User input ; input function used
calculation_to_units = 24 * 60 * 60 # no need to specify the datatype, python automatically picks the data type unlike other languages
name_of_unit = "seconds"

def days_to_units(num_of_days):
    print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}")

user_input = input("Hey user, enter a number of days and I will conver it to seconds!\n")
print(user_input)

# Function with Return Values
calculation_to_units = 24 * 60 * 60 # no need to specify the datatype, python automatically picks the data type unlike other languages
name_of_unit = "seconds"

def days_to_units(num_of_days):
    return(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}")

my_var = days_to_units(35)
print(my_var)

# Function with Return Values
# User input ; input function used
calculation_to_units = 24 * 60 * 60 # no need to specify the datatype, python automatically picks the data type unlike other languages
name_of_unit = "seconds"

def days_to_units(num_of_days):
    return(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}")

# input values we give in input is always treated as a string not number, so we need specify int
user_input = input("Hey user, enter a number of days and I will conver it to seconds!\n")
user_input_number = int(user_input)

calculated_values = days_to_units(user_input_number)
print(calculated_values)

# Restricting users to only add spefic  input
# Validate User input
# Using "Conditionals" if and else
calculation_to_units = 24 * 60 * 60 # no need to specify the datatype, python automatically picks the data type unlike other languages
name_of_unit = "seconds"

def days_to_units(num_of_days):
    conditional_check = num_of_days > 0
    print(type(conditional_check))
    if num_of_days > 0:    # conditional
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"
    else:
        return "you entered negative value, so no convertion for you"


# input values we give in input is always treated as a string not number, so we need specify int
user_input = input("Hey user, enter a number of days and I will conver it to seconds!\n")

calculated_values = days_to_units(int(user_input))
print(calculated_values)

# Two equal signs and conditionals
calculation_to_units = 24 * 60 * 60 # no need to specify the datatype, python automatically picks the data type unlike other languages
name_of_unit = "seconds"

def days_to_units(num_of_days):
    conditional_check = num_of_days > 0
    print(type(conditional_check))
    if num_of_days > 0:    # conditional
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"
    elif num_of_days == 0:   # two equal signs when checking if equals
        return "you entered 0, please enter valid positive value"
    else:
        return "you entered negative value, so no convertion for you"


# input values we give in input is always treated as a string not number, so we need specify int
user_input = input("Hey user, enter a number of days and I will conver it to seconds!\n")

calculated_values = days_to_units(int(user_input))
print(calculated_values)

# validate users input
calculation_to_units = 24 * 60 * 60 # no need to specify the datatype, python automatically picks the data type unlike other languages
name_of_unit = "seconds"

def days_to_units(num_of_days):
    conditional_check = num_of_days > 0
    print(type(conditional_check))
    if num_of_days > 0:    # conditional
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"
    elif num_of_days == 0:   # two equal signs when checking if equals
        return "you entered 0, please enter valid positive value"
    else:
        return "you entered negative value, so no convertion for you"


# input values we give in input is always treated as a string not number, so we need specify int
user_input = input("Hey user, enter a number of days and I will conver it to seconds!\n")
# validation of user input
if user_input.isdigit():
    user_input_number = int(user_input)
    calculated_values = days_to_units(user_input_number)
    print(calculated_values)
else:
    print("Your input is not a number, Don't ruin my program")

# Cleanup
# validate users input
calculation_to_units = 24 * 60 * 60 # no need to specify the datatype, python automatically picks the data type unlike other languages
name_of_unit = "seconds"

def days_to_units(num_of_days):
    if num_of_days > 0:    # conditional
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"
    elif num_of_days == 0:   # two equal signs when checking if equals
        return "you entered 0, please enter valid positive value"

def validate_and_execute():
    if user_input.isdigit():
        user_input_number = int(user_input)
        calculated_values = days_to_units(user_input_number)
        print(calculated_values)
    else:
        print("Your input is not a number, don't ruin my program")


# input values we give in input is always treated as a string not number, so we need specify int
user_input = input("Hey user, enter a number of days and I will conver it to seconds!\n")
validate_and_execute()

# Nested if else
# validate users input
calculation_to_units = 24 * 60 * 60 # no need to specify the datatype, python automatically picks the data type unlike other languages
name_of_unit = "seconds"

def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"

def validate_and_execute():
    if user_input.isdigit():
        user_input_number = int(user_input)
        if user_input_number > 0:  # conditional
            calculated_values = days_to_units(user_input_number)
            print(calculated_values)
        elif user_input_number == 0:  # two equal signs when checking if equals
            print("you entered 0, please enter valid positive value")
    else:
        print("Your input is not a number, don't ruin my program")


# input values we give in input is always treated as a string not number, so we need specify int
user_input = input("Hey user, enter a number of days and I will conver it to seconds!\n")
validate_and_execute()

# try except; Also known as try catch in other programing laguange
calculation_to_units = 24 * 60 * 60 # no need to specify the datatype, python automatically picks the data type unlike other languages
name_of_unit = "seconds"

def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"

def validate_and_execute():
    try:

        user_input_number = int(user_input)
        if user_input_number > 0:  # conditional
            calculated_values = days_to_units(user_input_number)
            print(calculated_values)
        elif user_input_number == 0:  # two equal signs when checking if equals
            print("you entered 0, please enter valid positive value")
        else:
            print("you entered a negative number, no conversion for you")
    except ValueError:
        print("Your input is not a number, don't ruin my program")


# input values we give in input is always treated as a string not number, so we need specify int
user_input = input("Hey user, enter a number of days and I will conver it to seconds!\n")
validate_and_execute()

# while loop; execute a set of statements as long as a condition is true
#  Let user exit the program
calculation_to_units = 24 * 60 * 60 # no need to specify the datatype, python automatically picks the data type unlike other languages
name_of_unit = "seconds"

def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"

def validate_and_execute():
    try:

        user_input_number = int(user_input)
        if user_input_number > 0:  # conditional
            calculated_values = days_to_units(user_input_number)
            print(calculated_values)
        elif user_input_number == 0:  # two equal signs when checking if equals
            print("you entered 0, please enter valid positive value")
        else:
            print("you entered a negative number, no conversion for you")
    except ValueError:
        print("Your input is not a number, don't ruin my program")

user_input = ""    # so while loop doesn't through error
while user_input != "exit":
    user_input = input("Hey user, enter a number of days and I will conver it to seconds!\n")
    validate_and_execute()

# List ; to store multiple items in a single variable
#  A list can contain different data types
# For loop = used for iterating over a sequence; so we can execure smth for each item in a list
calculation_to_units = 24 * 60 * 60 # no need to specify the datatype, python automatically picks the data type unlike other languages
name_of_unit = "seconds"

def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"

def validate_and_execute():
    try:
        user_input_number = int(num_of_days_element)
        if user_input_number > 0:  # conditional
            calculated_values = days_to_units(user_input_number)
            print(calculated_values)
        elif user_input_number == 0:  # two equal signs when checking if equals
            print("you entered 0, please enter valid positive value")
        else:
            print("you entered a negative number, no conversion for you")
    except ValueError:
        print("Your input is not a number, don't ruin my program")

user_input = ""    # so while loop doesn't through error
while user_input != "exit":
    user_input = input("Hey user, enter a number of days as a comma separated list and I will conver it to seconds!\n")
    print(type(user_input.split(",")))
    print(user_input.split(","))
    for num_of_days_element in user_input.split(","):      # split function will take the string "10,20,50,100" and convert into list [10, 20, 50, 100]
        validate_and_execute()     # to excute just add 10 20 30 with space or commans if we add it in split funtion

# List examples and append to add values to the vairable
my_list =["January", "February", "March"]
print(my_list[2])
my_list.append("Apirl")   # add values to the list
print(my_list)