# pands-weekly-tasks

This is the repository of Aoife Flavin. The purpose of this repoitory is to complete the weekly problem sets given in the module Programming and Scripting, in Semester 1 of the Higher Diploma in Data Analytics at ATU.

In each section I will detail my approach to solving the assigned tasks, cite the sources I used while problem-solving, and provide an overview of the technologies used in both code creation and testing.

I have previously completed very basic python training so some tasks did not require extensive research.


## Table of Contents
* bank.py
* accounts.py
* collatz.py
* weekday.py
* squareroot.py
* Task 7
* task 8
(make these links once this is filled out more)

---

### ***Bank***
    Write a program called bank.py 
    The program should:
    a. Prompt the user and read in two money amounts (in cent)
    b. Add the two amounts
    c. Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 

### Description:
The bank.py program is a simple utility that allows users to add two monetary amounts and display the result in a human-readable format. When called it asks the user to input an amount in cent, then asks for another amount in cent. The program adds these cent amounts together, then uses the // function to fnd the Euro amount and the % function to find the remaining sent amount. The result is then formatted and printed

<details>
           <summary>User point of view</summary>
           <p>

User call of the program is :

```
λ python bank.py
```
User input :
```
Enter amount one (in cent): 75
Enter amount two (in cent): 99
```
and the output is :

```
The sum of these amounts is: €1.74
```
</p>
</details>

#### Sources:
n/a

### ***Accounts***
    Write a python program called accounts.py that reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).
    Modify the program to deal with account numbers of any length.

### Description:
This program begins by asking the user to input a 10 digit number, as a string. The program then takes this input and turns it from a string to a list. It then slices the first 6 items in the list using indexing and replaces the characters with X's. Finally the join() method is used to turn the list back into a string, with no spaces between the letters.

For this program to read in an account number of any length, and stll replace all numbers except the last four, the process is mostly the same. The difference lies in the indexing used when slicing the list. For a list of any size the program is told to replace all numbers with X's ***except*** the last four.

<details>
           <summary>User point of view</summary>
           <p>

User call of the program is :

```
λ python accounts.py
```
User input :
```
Please enter an 10 digit account number: 1234567890
```
and the output is :

```
XXXXXX7890
```
User input :
```
Please enter an account number of any length:997843984584593893
```
and the output is :

```
XXXXXXXXXXXXXX3893
```

</p>
</details>

#### Sources:
https://www.geeksforgeeks.org/python-program-convert-string-list/
https://www.geeksforgeeks.org/how-to-replace-values-in-a-list-in-python/

### ***Collatz*** 
    Write a program, called collatz.py, that asks the user to input any positive integer and outputs the successive values of the following calculation.
    At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
    Have the program end if the current value is one.

### Description:
This program prompts the user to input a positive integer. If the user enters a negative integer, the program requests a positive value until a valid input is provided. Once a positive integer is entered, the program enters a while loop. Within the loop, the program continuously outputs the current number with a space next to it while performing calculations.

Using an if statement, the program checks whether the current number, when divided by two, results in no remainder. If so, the number is divided by two. If there is a remainder, indicating an odd number, the number is multiplied by three and one is added. This process continues until the number becomes one, at which point the loop exits.

<details>
           <summary>User point of view</summary>
           <p>

User call of the program is :

```
λ python collatz.py
```
User input :
```
Please enter a positive integer: 10
```
and the output is :

```
10 5 16 8 4 2 1
```
</p>
</details>

#### Sources:
https://www.geeksforgeeks.org/loops-in-python/

### ***Weekday*** 
    Write a program that outputs whether or not today is a weekday.

### Description:
xxxFILL IN DESCRIPTIONxxx

<details>
           <summary>User point of view</summary>
           <p>

User call of the program is :

```
λ python weekday.py
```
If ran on a weekday the output is:
```
Yes, unfortunately today is a weekday.
```
If ran on the weekend the output is:

```
It is the weekend, yay!
```
</p>
</details>

#### Sources:
FILL IN SOURCES

### ***Square Root***
    Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
    Create your own sqrt function, do not use the built in functions x ** .5 or math.sqrt(x).

### Description:
xxxFILL IN DESCRIPTIONxxx

<details>
           <summary>User point of view</summary>
           <p>

User call of the program is :

```
λ python collatz.py
```
User input :
```
Please enter a positive integer: 10
```
and the output is :

```
10 5 16 8 4 2 1
```
</p>
</details>

#### Sources:
FILL IN SOURCES


### ***Count E's***
    Write a program that reads in a text file and outputs the number of e's it contains.
    The program should take the filename from an argument on the command line.

### Description:
This program reads a text file (in this case I had it read Moby Dick), and counts the number of times the letter 'e' occurs.
This was done by first creating a function that opens a file, reads it and records the number of times a particular letter occurs.
If the file does not exist a File not found error occurs.
The main part of the program takes the file, that has been passed as an argument and assigns it to a variable. 
The function that was created earlier is called with the variable assigned to the letter e, which has the program count all the e's in the text file.
Finally, the result is printed out.



<details>
           <summary>User point of view</summary>
           <p>

User call of the program is :

```
λ python count_es.py mobydick.txt
```

and the output is :

```
The letter e occurs 58820 times in mobydick.txt
```
</p>
</details>

#### Sources:
https://www.sanfoundry.com/python-program-read-contents-file/
https://moez-62905.medium.com/the-ultimate-guide-to-command-line-arguments-in-python-scripts-61c49c90e0b3
https://www.w3schools.com/python/python_try_except.asp
https://gist.github.com/StevenClontz/4445774
https://docs.python.org/3/library/exceptions.html

### ***Square Root***
    Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
    Create your own sqrt function, do not use the built in functions x ** .5 or math.sqrt(x).

### Description:
xxxFILL IN DESCRIPTIONxxx

<details>
           <summary>User point of view</summary>
           <p>

User call of the program is :

```
λ python collatz.py
```
User input :
```
Please enter a positive integer: 10
```
and the output is :

```
10 5 16 8 4 2 1
```
</p>
</details>

#### Sources:
https://www.geeksforgeeks.org/plot-multiple-plots-in-matplotlib/