# Programmer: Teresa Fischer
# Date: 10/29/24
# Program #2: Random Number File Writer

# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500.
# The application should let the user specify how many random numbers the file will hold
# (up to 1000).

import random

def random_numbers_writer():

    user_input = int(input("How many random numbers should this file hold? (0 - 1000):"))
    with open('rand_numbers.txt', 'w') as rand_file:
        for i in range(user_input):
            rand_file.write(str(random.randint(1, 500)) + "\n")

    print('Look at the random_numbers text file to see your numbers!')

if __name__ == '__main__':
    random_numbers_writer()
