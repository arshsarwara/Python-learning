# Sets- another built-in data type of python
# as with lists, used to store multiple items of data
# Difference from list, Duplicate values not allowed
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
    list_of_days = user_input.split(", ")
    print(list_of_days)
    print(set(list_of_days))
    print(type(list_of_days))
    print(type(set(list_of_days)))

    for num_of_days_element in set(list_of_days):      # split function will take the string "10,20,50,100" and convert into list [10, 20, 50, 100]
        validate_and_execute()     # to excute just add 10 20 30 with space or commans if we add it in split funtion
