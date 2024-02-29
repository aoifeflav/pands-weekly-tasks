# weekday.py
# Outputs whether or not today is a weekday
# Author: Aoife Flavin

import datetime

#define function
def is_weekday():
    #current date                  assigns 0-6
    today = datetime.datetime.now().weekday()

    #check if weekday 0-4 = monday to friday
    if today <= 4:
        return True
    else:
        return False
    
if is_weekday():
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")