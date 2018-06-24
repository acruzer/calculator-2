"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
# input_string = input ("Enter you Calculation:")

# token = input_string.split(" ")
def calculator():
	input_string = input ("Enter you Calculation: ")

	token = input_string.split(" ")	
	if token[0] == "pow":
		result = power (int(token[1]), int(token[2]))
	# print (token)
		print (result)

calculator()