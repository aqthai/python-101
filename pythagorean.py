#
# Author: Alvin Thai
# Description: 
#    This code can compute the hypotenuse length of a right triangle given the lengths of the two sides that form the right angle.  It uses input, assigning of a variable, and functions.
#

def print_hyp_length(): 
    X = input("Enter first side: ")
    Y = input("Enter second side: ")  
    Z = (int(X)**2 + int(Y)**2)**0.5              
    print((int(X)**2 + int(Y)**2)**0.5)
#This function calculates and prints the hypotenuse after inputting variables X and Y.

def main():     
    X = input("Enter first side: ")
    Y = input("Enter second side: ") 
    Z = (int(X)**2 + int(Y)**2)**0.5 
    print("The hypotenuse of a right triangle is length " + str(Z) + " when the other two sides are of length " + str(X) + " and " +str(Y))
main()
#The variable Z is assigned to the hypotenuse length to fit the main function.