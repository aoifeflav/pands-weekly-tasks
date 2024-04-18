#count_es.py
#reads in a text file and outputs the number of e's it contains.
#Author: Aoife Flavin

#Need to download a text file to the device, in the same repository?
#The program needs to read the file, line by line and count the Es
#First try without error handling, add this later

#import the sys module
import sys


#create a function that takes the file name and letter as parameters
def count_es(filename, letter):
    try:
        with open(filename, 'r') as file: #open file in read mode
            text = file.read() #reads the file and stores it in the variable text
            return text.count(letter) #returns no. of times the letter occurs
    except FileNotFoundError:
        print("File not found")    
        

filename = sys.argv[1] #assigns the filename to the variable
letter_to_count = "e" #could change this to count any letter
count = count_es(filename, letter_to_count) #calls function from above, to count Es
if count is not None:
    print(f"The letter {letter_to_count} occurs {count} times in {filename}") #print