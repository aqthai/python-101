#
# Author: Alvin Thai
# Description:
#     Uses list and 2-d list to re-write text images in backwards and/or upside-down order limited to the functions len(), list(), and append().
#
def file_input():
    image = input("Select an image file: ")
    output = input("Select an output file: ")
    direction = input("Select a direction (lr, ud): ")
    i = open(image, 'r')
    lines = i.readlines()
    return image, output, direction, lines
# takes variables for the text image, output file, and direction and then returns them and the image as a list 
def ud_flip(image, output, direction, lines):
    pixels = []
    for line in lines:
        pixels.append(line.strip("\n"))
    count = len(pixels) - 1
    w = open(output, 'w')
    while count >= 0:
        for line in lines:
            w.write(str(pixels[count]) + "\n")   
            count -= 1
# This writes an image into another file starting with the bottom of the list 'pixels' to provide an image flipped top-to-bottom.        
def lr_flip(image, output, direction, lines):
    pixels = []
    for line in lines:
        pixels.append(line.strip("\n"))   
    w = open(output, 'w')
    for i in range(0, len(pixels)):
        count = len(line)-1    
        while count >= 0:
            w.write(str(pixels[i][count]))    
            count -= 1
        w.write("\n")    # starts a new line right after every row is being written
# This writes lines starting with characters at the end of the row in pixels to provide an image flipped left-to-right. The count variable is right before the while loop, so that count is reestablished after every cycle.    
def main():
    image, output, direction, lines = file_input()
    if direction == ('lr'):
        lr_flip(image, output, direction, lines)
    elif direction == ('ud'):
        ud_flip(image, output, direction, lines)
    while direction != ('ud') and direction != ('lr'):
        print("Warning: provide proper input (lr, ud)")
        image, output, direction, lines = file_input()
# Asks user to imput image text file, output file name, and direction change.  If an invalid direction change is given, it will give a warning message and ask the user to provide valid input.
main()
        