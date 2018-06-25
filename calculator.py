"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


def input_string():
	"""This function takes in a string and splits it into a list
	and returns that list."""
	input_string = input ("Enter your Calculation: ")
	token = input_string.split(" ")
	
	return token

def check_len():
	"""Checks the length of the list returned from input_string function
	and assigns variables and returns them."""
	operator, num1, num2 = None, None, None
	token = input_string()
	if len(token) >= 1:
		operator = token[0]
	if len(token) >= 2:
		num1 = int(token[1])
	if len(token) >= 3:
		num2 = int(token[2])
	return operator, num1, num2


def calculator():
	"""Performs calculations based on variables from check_len function."""
	while True:	
		operator, num1, num2 = check_len()

		if operator == "+":
			result = add (num1, num2)
				
		elif operator == "-":
			result = subtract (num1, num2)
				
		elif operator == "*":
			result = multiply (num1, num2)

		elif operator == "/":
			result = divide (num1, num2)

		elif operator == "square":
			result = square (num1)

		elif operator == "cube":
			result = cube (num1)

		elif operator == "pow":
			result = power (num1, num2)

		elif operator == "mod":
			result = mod(num1, num2)

		elif operator == "q":
			break


		print (result)

calculator()