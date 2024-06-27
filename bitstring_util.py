# This module is used for generating a random bitstring of a specified size.
#
# Code originally from https://www.geeksforgeeks.org/python-program-to-generate-random-binary-string/
# and contributed by Edula Vinay Kumar Reddy.
#
# Modified to handle leading zeroes.

import random


def generate_binary_string(n):
    # Generate a random number with n bits
    number = random.getrandbits(n)

    # Convert the number to binary
    binary_string = format(number, "0b")

    # handle leading zeroes
    if len(binary_string) != n:
        binary_string = ("0" * (n - len(binary_string))) + binary_string

    return binary_string
