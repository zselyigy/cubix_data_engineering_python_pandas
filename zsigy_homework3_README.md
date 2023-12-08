# Homework 3 - Week 3
Created by István Gy. Zsély, version 0.1

# Project overview
This code was created during my participation in the [CUBIX Data Engineering course](https://courses.cubixedu.com/kepzes/data-engineer-23q4).

The aim is to demonstrate the knowledge about the basic features of Python, like loops, conditionals, error handling, user input, own functions by writing a python code which asks the user to input data and make calculations with that.

The following tasks are performed by the program, denoted in comments in the source code:

 1. Ask the user to type an INTEGER number between 1 and 30 (INPUT).
 2. Check if the input is correct:  
 
    a. If the user inputs a TEXT, print a message: 'Type a NUMBER, not a text!'.

    b. If the user inputs a number which is NOT INTEGER, print a message: 'Number must be INTEGER!'.

    c. If the user inputs an integer NOT BETWEEN 1 AND 30, print a message: 'Number must be BETWEEN 1 and 30!'.

    Remember that the input data is a STRING by default, so if you need to calculate with it, you need to convert it to FLOAT or INT, e.g.: float(n), int(n).

3. Use a WHILE loop to ask for input again and again in case of invalid inputs, until the input is valid.

4. Create a CUSTOM FUNCTION named ‘is_divisible(number, divisor)’ which checks if the number is divisible by the divisor, if divisible, it should return True(otherwise False).

5. Then use FOR loop to loop through the integer numbers between 1 and the number typed by the user, and by using the custom function you created.  

    a. Print all the EVEN numbers between 1 and the number typed by the user

    b. Print all the numbers DIVISIBLE BY 3 between 1 and the number typed by the user
