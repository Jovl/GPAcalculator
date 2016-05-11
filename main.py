"""
File: main.py

Author: Jeremiah Lantzer

Description: This program is intended to
be a GPA calculator that will calculate
individual GPAs and cumulative GPAs.

Purpose: Summer Project week #1

Variables: gpa[], count, response, continueVar

Functions: checkvalid(to be added later, will check the validity of response)
"""

gpa = list()  # currently empty list will hold all inputted GPAs
count = 0  # count will track how many GPAs have been entered
response = 'y'  # will be used to check whether the user wants to add another GPA to the list
continueVar = True


# function will check to make sure the user continue input is valid
def checkvalid(resp):
    if resp == 'y' or resp == 'Y':  # if y or Y is entered the program continues
        return True
    elif resp == 'n' or resp == 'N':  # if n or N is entered the program stops
        return False
    else:  # anything else must be reentered
        return 0


while continueVar:  # loop will run as long as continueVar is true

    gpa[count] = float(
        input('Please enter a GPA: '))  # asks the user for a GPA. stores it as a float types in the list
    print

    response = input('Would you like to continue? y/n: ')
    print
    continueVar = checkvalid(response)
    # TODO: add in loop to check result again

    count += 1  # count increases after each iteration to cycle through the GPA list
