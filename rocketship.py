#
# Author: Alvin Thai
# Description:
#     The program takes an integer input, returns it as a variable to be used in three other functions that print out while loop patterns that vary in height and width depending on the integer input.  The integer input is used to print a rocketship.
#
def get_rocket_size():
    X = int(input("Enter rocket size: "))
    return X
# This function accpets and returns variable X as the rocket size.

def get_rocket_cap(X):
    index = 1
    total_lines = (X * 2) - 1
    while index <= total_lines:
        print(' ' + ' ' * (total_lines - index) + "/" * index + "**" + "\\" * index)
        index += 1
# This function prints the rocket cap.  The total lines it occupies were calculated before inserting it into a while loop.  The index tells it when to stop printing lines.

def get_upper_tube(X):
    print("*" + '=' * (X * 4) + "*")
    index = 1
    tube_lines = X * 2
    while index <= X:
        print("|" + "." * (X - index) + "/\\" * index + "." * (X * 2 - 2 * index), end="")
        print("/\\" * index + "." * (X - index) + "|")
        index += 1
    index -= 1
    while index >= 1:
        print("|" + "." * (X - index) + "\\/" * index + "." * (X * 2 - 2 * index), end="")
        print("\\/" * index + "." * (X - index) + "|")
        index -= 1
# This prints the upper half of the rocket.  Its width and height depends on the integer input of the first function and are limited by the boolean statement within the while loop.  WHile loop functions print out the upper and bottom patterns of the rocketship half while an index -= 1 statement removes an extra index addition.

def get_lower_tube(X):
    print("*" + '=' * (X * 4) + "*")
    index = 1
    while index <= X:
        print("|" + "." * (index - 1) + "\\/" * (X - index + 1) + "." * ((index - 1) * 2), end="")
        print("\\/" * (X - index + 1) + "." * (index -1) + "|")
        index += 1
    index -= 1
    while index >= 1:
        print("|" + "." * (index - 1) + "/\\" * (X - index +1) + "." * ((index - 1) * 2), end="")
        print("/\\" * (X - index + 1) + "." * (index -1) + "|")
        index -= 1
    print("*" + '=' * (X * 4) + "*")
# Thsi prints the lower half of the rocket.  It has borders established by the "=" sign that varies in width depending on the rocket size input.  While loops functions print out the upper and bottom part patterns of the rocketship half.  

def main():
    X = get_rocket_size()
    print()
    get_rocket_cap(X)
    get_upper_tube(X)
    get_lower_tube(X)
    get_rocket_cap(X)
main()
# The print statment adds space between getting the rocket size and the rocketship.  The functions within main are in the order they get printed.


