"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
# input_string = input ("Enter you Calculation:")

# token = input_string.split(" ")
def input_string():
	input_string = input ("Enter your Calculation: ")
	token = input_string.split(" ")
	
	return token

def calculator():

	while True:
		token = input_string()	
		operator = token[0]
		num1 = int(token[1])
		num2 = int(token[2])	
		
		if operator == "+":
			result = add (num1, num2)
				
		elif operator == "-":
			result = subtract (num1, num2)
				
		elif operator == "*":
			result = multiply (num1, num2)

		elif operator == "q":
			break

		# input_string = input ("Enter you Calculation: ")
		# token = input_string.split(" ")

		# print (token)
		print (result)
	# input_string()

# input_string()
calculator()