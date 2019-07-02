#
# Author: Alvin Thai
# Description:
#     Uses a for loop to assign indexes to lines from two separate text files into a dictionary and then uses another for loop to write the dictionary contents in order into another text file.
#
#import collections
def unmix():
    mixed_file = input("Enter the name of the mixed text file: ")
    mixed_index = input("Enter the mix index file: ")
    f = open(mixed_file, 'r')
    lines = f.readlines()
    i = open(mixed_index, 'r')
    indexes = i.readlines()
    encrypt_dictionary = {}
    for l in range(0, len(lines)):
        encrypt_dictionary[indexes[l]] = lines[l]   # adds lines from text file into dictionary
    
    d = open('decrypted.txt', 'w')      
    for line in range(1, len(encrypt_dictionary)+1):     # a for loop is used to write onto the new text file.  It starts its range at 1 to match with the keys from the dictionary.  The +1 will make the last line inclusive.
        d.write(encrypt_dictionary[str(line) + '\n'])    # '\n' will have the for loop writing onto a new line after every line is finished
            
def main():
    unmix()
main()