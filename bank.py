# bank.py 
# Finds the sum of two integers
# Week 2 task
# Author: Aoife Flavin

#Name & Enter the first input, make sure it's an integer
amount1 = int(input("Enter amount one (in cent):"))
#Name & Enter the next input as an int
amount2 = int(input("Enter amount two (in cent):"))
#add to get total
total = amount1 + amount2

#divide the total by 100 using int divider to get euros
euros = total // 100
#Use the % to get the remainder, that will be the cents
cent = total % 100

#format it as a string
print("The sum of these amounts is: " + "€" + str(euros) + "." + str(cent))

