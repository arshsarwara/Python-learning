# modules is just a python file that contains functions or variables athat we can use in another python file

def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    else:
        return "unsupported unit"
def validate_and_execute(days_and_unit_dictionary):
    try:
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:  # conditional
            calculated_values = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
            print(calculated_values)
        elif user_input_number == 0:  # two equal signs when checking if equals
            print("you entered 0, please enter valid positive value")
        else:
            print("you entered a negative number, no conversion for you")
    except ValueError:
        print("Your input is not a number, don't ruin my program")

user_input_message = "Hey user, enter a number of days and conversion unit!\n"