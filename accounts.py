# accounts.py
# Reads a 10 character account number and outputs with only the last 4 digits showing
# Author: Aoife Flavin

account_no = str(input("Please enter a 10 digit account number:"))

#Turn it into a list, replace the values with X then turn it back into a string??

#Turn into list
listed = list(account_no)

#Replace first 6 values
listed[:6] = ["X"] * len(listed[:6])

#Turn back into string
output = "".join(listed)

print(output)

# To deal with an account number of any length change the code
# to replace everything EXCEPT the last 4 with Xs

account_no2 = str(input("Please enter an account number of any length:"))

#Turn into list
listed2 = list(account_no2)

#Replace all but last 4 value
listed2[:-4] = ["X"] * len(listed2[:-4])

#Turn back into string
output2 = "".join(listed2)

print(output2)
