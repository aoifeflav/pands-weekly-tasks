#squareroot.py
# Create a function that finds the square root of a function without using
#built in functions
#Author: Aoife Flavin

#define the function
def sqrt(number):
    if number < 0:  
        raise ValueError("Cannot compute") # value error in case negative number is used
    
    #Square root of 0 is 0
    if number == 0:
        return 0
    
    estimate = number / 2 #Initial guess
    difference = 1e-10 #How accurate you want the estimate to be

    #start the loop
    while True:
        estimate_two = 0.5 * (estimate + (number / estimate)) #Newton formula
        if abs(estimate_two - estimate) < difference: #checks if it is close enough
            break
        #for the next iteration
        estimate = estimate_two

    return estimate_two

#Testing

#input number to find sq root
number_input = float(input("Please enter a positive number:"))


if number_input <= 0:
    print("Input must be a positive number.") #error
else:
    result = sqrt(number_input) 
    print(f"The square root of {number_input} is approx {result}")
