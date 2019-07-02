# 
# Author: Alvin Thai
# Description:
#     Imports text files, creates a list of words from the first one and a 2d list from the second one, creates strings from rows, columns, and the diagonals from the upperleft to lower right corners of the 2d list and uses the find method for words that are in the list of words, then prints the found word one per line.
#
def occurs_in(s, L):
    for word in L:
        word = word.lower()   
        if s.find(str(word)) >= 0:
            print(word)
        word_upper = word.upper()  
        if s.find(str(word_upper)) >= 0:
            print(word_upper)
# This function checks if a word in list 'L' is found in the string 's'.  Word is lowercased to regulate cap-size.  If the grid is comprised of uppercased letters, then it will print the word with uppercased letters.

def imports_list():
    filename = input()
    w = open(filename)      
    words = w.readlines()
    L = []
    for word in words:
        word = word.strip("\n")
        L.append(word)
    return L
# creates a list of words L without "\n"

def imports_grid():
    row = ""
    filename = input()
    g = open(filename)
    letters = g.readlines()
    text = ""
    grid = []
    for l in letters:
        l = l.rstrip("\n")
        row = l.split()   
        grid.append(row)  
    return grid
# makes a 2d list from the imported grid file

def checks_horizontal(L, grid):
    text = ""
    index = 0
    while index != len(grid):
        for i in range(0, len(grid)):
            text += grid[index][i]
        occurs_in(text, L)
        text = ""         # resets text to allow reading of string from next row
        index += 1        # moves to next row of grid
# creates the string 'text' from rows going left to right and checks if a word from list 'L' is in the string

def checks_horizontal_backwards(L, grid):
    text = ""
    index = 0
    count = len(grid)-1   # targets the last index of the grid rows
    while index != len(grid):
        while count >= 0:
            text += grid[index][count]
            count -= 1
        occurs_in(text, L)
        text = ""
        index += 1
        count = len(grid)-1    # resets count to start at the right
# looks for words from rows right to left  
        
def checks_columns_updown(L, grid):
    text = ""
    index = 0
    while index != len(grid):
        for i in range(0, len(grid)):
            text += grid[i][index]
        occurs_in(text, L)
        text = ""
        index += 1
# looks for words from top to bottom

def checks_columns_downup(L, grid):
    text = ""
    index = 0
    count = len(grid)-1    # count targets a row starting from the bottom
    while index != len(grid):
        while count >= 0:
            text += grid[count][index]
            count -= 1
        occurs_in(text, L)
        text = ""
        index += 1
        count = len(grid)-1
# looks for words from bottom to top

def checks_diagonal_UL_LR(L, grid):
    text = ""
    index = 0
    for j in range(0, len(grid)-1):
        while j < len(grid) and index < len(grid):
            text += grid[j][index]
            j += 1
            index += 1
        occurs_in(text, L)
        text = ""
        index = 0
    for i in range(1, len(grid)-1):
        while i < len(grid) and index < len(grid):
            text += grid[index][i]
            i += 1
            index += 1
        occurs_in(text, L)
        text = ""
        index = 0
# checks diagonals from upperleft to lower right for words

def main():
    a = imports_list()
    b = imports_grid()
    checks_horizontal(a, b)
    checks_horizontal_backwards(a, b)
    checks_columns_updown(a, b)
    checks_columns_downup(a,b)
    checks_diagonal_UL_LR(a, b)
main()