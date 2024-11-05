# Programmer: Teresa Fischer
# Date: 10/29/24
# Program #1: Item Counter

# Assume a file containing a series of names (as strings) is named names.txt
# (Use the included example file names.txt) and exists on the computer's disk.
# Write a program that displays the number of names that are stored in the file.

def count_file_lines():
    ######################
    with open('names.txt', 'r') as file_lines:
        number_of_names = 0
        number_of_names = len(file_lines.readlines())
    ######################
    print(f'There are {number_of_names} names in the count_file_lines function')

# You don't need to change anything below this line:
if __name__ == '__main__':
    count_file_lines()
