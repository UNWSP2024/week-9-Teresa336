# Programmer: Teresa Fischer
# Date: 10/29/24
# Program #3: Average Numbers

# Assume a file containing a series of integers is named numbers.txt and exists on the computer's disk.
# (please use the provided numbers.txt)
# Write a program that reads all of the numbers stored in the file and calculates their total.  

# The program should handle the following exceptions: 

# It should handle any IOError exceptions that are raised.
# It should handle any ValueError exceptions that are raised when the items that are read from the file 
# are converted to a number.
def sum_numbers_from_file():
    ######################
    total = 0
    with open("numbers.txt", "r") as number_list:
        for line in number_list:
            try:
                number = float(line)
                total += number
            except IOError:
                print('There was an error. That file does not exist.')
                pass
            except ValueError:
                print('Value Error:')
                print(f"There was a problem converting ({line}) to a number.")
    ######################
    print(f'The total in the sum_numbers_from_file function is {total}')

# You don't need to change anything below this line:
if __name__ == '__main__':
    sum_numbers_from_file()
    