#
# Author: Alvin Thai
# Description:
#     This code finds the distance between two points when the coordinates are input into the function.  It uses input, variables, and functions.
#

def distance(): 
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))    
    print((x2 - x1)**2 + (y2 - y1)**2)**0.5
#This function calculates the distance between two coordinate points.   

def main():
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))
    A = ((x2 - x1)**2 + (y2 - y1)**2)**0.5 
    print("The distance between (" + str(x1) + "," + str(y1) + ") and (" + str(x2) + "," + str(y2) + ") is " + str(A) + ".")
main()
# Variable A is assigned to distance to fit into the main function.