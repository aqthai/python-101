#
# Author: Alvin Thai
# Description:
#    This code computes volume A of a cube a three dimensional box figure with any dimensions after assigning numerical values to variables X, Y, and Z using input and functions.
#

def volume():                               #This function calculates and prints volume given values for X, Y , and Z.
    X = input("Enter width: ")
    Y = input("Enter height: ")
    Z = input("Enter length: ")    
    print("int(X) * int(Y) * int(Z)")
    
def main():
    X = input("Enter width: ")
    Y = input("Enter height: ")
    Z = input("Enter length: ")
    A = int(X) * int(Y) * int(Z)            # Variable A is assigned to volume to fit the main function.
    print("The volume of a cube with width " + str(X)+", height " + str(Y) + ", and length " + str(Z)+" is " + str(A) )
main()

