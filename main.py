"""
File: main.py

Author: Jeremiah Lantzer

Description: This program is intended to
be a GPA calculator that will calculate
individual GPAs and cumulative GPAs.

Purpose: Summer Project week #1

Variables: gpas[], count, response

Functions: checkValid(to be added later, will check the validity of response)
"""

gpas = list()  # currently empty list will hold all inputted GPAs
count = 0  # count will track how many GPAs have been entered
response = 'y'  # will be used to check whether the user wants to add another GPA to the list

while response == 'y':

    count += 1
