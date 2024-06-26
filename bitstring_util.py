# This module is used for generating a random bitstring of a specified size.
# Code originally from https://www.geeksforgeeks.org/python-program-to-generate-random-binary-string/
# and contributed by Edula Vinay Kumar Reddy

import random

def generate_binary_string(n):
	# Generate a random number with n bits
	number = random.getrandbits(n)
	# Convert the number to binary
	binary_string = format(number, '0b')
	return binary_string

