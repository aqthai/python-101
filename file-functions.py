# 
# Author: Alvin Thai
# Description:
#     Performs functions with text files by opening them through variables and turning them into accessible lists.
# 
def count_lines(file_name):
    f = open(file_name, 'r')
    lines = f.readlines()
    count = 0
    for l in lines:
        count += 1
    return count
# Opens a file by assigning it to variables and increases count for each element in the list it creates.  The count is returned at the end.
def reverse_file(file_name):
    f = open(file_name, 'r')
    lines = f.readlines()
    new = ""
    for i in range(0, len(lines)):
        new = lines[i] + new
    print(new)
# An empty string is created and added to by using a for loop that is set in a range between 0 and the length of lines the file has.  An element is added to the string "new" each time through and then printed in reverse order.    
def search_file(file_name, word):
    f = open(file_name, 'r')
    lines = f.readlines()   
    count = 0
    for a in range(0, len(lines)):
        if lines[a].find(word) >= 0:
            count += 1
    return count
# Opens a file when calling the function and uses for loop and find method to increase a count for every line the word entered into the second parameter shows up.  A count for each line the word shows up is returned.