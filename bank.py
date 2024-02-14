# bank.py 
# Finds the sum of two integers
# Week 2 task
# Author: Aoife Flavin

amount1 = int(input("Enter amount one (in cent):"))
amount2 = int(input("Enter amount two (in cent):"))
total = amount1 + amount2

euros = total // 100
cent = total % 100

print("The sum of these amounts is: " + "€" + str(euros) + "." + str(cent))

