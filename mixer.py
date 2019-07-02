# 
# Author: Alvin Thai
# Description:
#     Encrypts using a randomizing algorithm and writes the lines and indexes of a python file into two separate text files.
#
from random import *
def mix():
    seed(123)    #randomizes 123 times when randint is used
    filename = input("Enter a name of a python program to mix: ")
    f = open(filename, 'r')
    lines = f.readlines()
    line_dictionary = {}
    index_dictionary = {}
    index = 1
    line_count = 0
    for line in lines:
        line_dictionary[index] = line.strip("\n")     #appends values into the dictionaries from the file and strips "\n" to swap properly
        index_dictionary[index] = index   #assigns an index value to each index in a separate dictionary
        index += 1
        line_count += 1
    for i in range(0, line_count*3):    
        index1 = randint(1, line_count)    
        index2 = randint(1, line_count)
        
        temp1 = line_dictionary[index1]    #stores temporarily
        temp2 = line_dictionary[index2]
        line_dictionary[index1] = temp2    #swaps the values
        line_dictionary[index2] = temp1
        
        temp3 = index_dictionary[index1]   #temporarily stores the value at this random index
        temp4 = index_dictionary[index2]   
        index_dictionary[index1] = temp4   #swaps the values which are indexes
        index_dictionary[index2] = temp3
        
    w = open('encrypted.txt', 'w')
    for line in line_dictionary:
        w.write(line_dictionary[line] + "\n")     #writes the mixed values of the dictionaries onto new files and adds "\n" to begin a new line after every line is written
    r = open('index.txt', 'w')
    for index_numbers in index_dictionary:
        r.write(str(index_dictionary[index_numbers]) + "\n")
        
def main():
    mix()
main()