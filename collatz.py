# collatz.py
# Takes any positive integer and outputs the successive values 
# Author: Aoife Flavin

#will need an if statement and a loop

#Have the user enter a number
number = int(input("Input any positive integer:"))

#Make sure its positive
if number <= 0:
    print("Please enter a positive integer")

#Start the loop
else:
    while number !=1: 
        print(number, end=' ') #keep it on the same line
        if number % 2 == 0: #if number is even
            number = (number // 2) #divide it by 2
        else:
            number = ((3 * number) + 1) #multiply by 3 and add 1
    print(1)

    