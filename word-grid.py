#
# Author: Alvin Thai
# Description:
#     Asks for grid dimensions and an integer, then randomizes the integer to generate a grid with lower-cased letters and commas in between
#
from random import*
#asks for grid size and integer input, 'seeds' the integer input, and returns n
def init():
    n = input()
    s = input()
    seed(s)    # randomizes s
    return int(n)

# makes a grid by appending letters into lists and appending the lists to another list
def make_grid(n):
    row = []
    g = []     #g is the variable for a grid this function will make at the end
    text = "abcdefghijklmnopqrstuvwxyz"
    for i in range(0, n):
        for j in range(0, n):
            a = text[randint(0,25)]     #a is a random letter from text
            row.append(a)               #a is appended to row
        g.append(row)                   #row is appended to grid
        row = []                        #row is reseted
    return g

# prints letters of the grid by concatenating lists with the join function
def print_grid(g):
    string_grid = ""
    for row in g:
        string_grid += (",".join(row) + "\n")   # concatenates joined rows of g
    print(string_grid)
        
def main():
    A = init()
    B = make_grid(A)
    C = print_grid(B)
    
main()


    
