'''
EXERCISE
1. Accept user input of goal and deadline
2. print back: how much time remaining until the deadline
'''

import datetime
# from datetime import datetime # as we're only using one function and drop the belo reference to module in below code

user_input = input("enter your goal with a deadline separated by colon\n") # user input is always interpreted as string
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_Date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.datetime.today()
time_till = deadline_Date - today_date
print(f"Dear user! Time remaing for your goal: {goal} is {time_till.days} days")
print(f"Dear user! Time remaing for your goal: {goal} is {int(time_till.total_seconds()/ 60 / 60)} hours")


