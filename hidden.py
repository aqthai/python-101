#
# Author: Alvin Thai
# Description:
#     Changes R,G,B values in 2D lists by using nested loops to reveal hidden messages within ppm files.
#
def template():
    image = input("Select an image file: ")
    output = input("Select an output file: ")
    channel = input("Channel: ")
    print("...")
    s = open(image, 'r')
    lines = s.readlines()
    pixels = []
    for line in lines:
        pixel = line.split()
        pixels.append(pixel)
    return image, output, channel, lines, pixels

def green(image, output, channel, lines, pixels):
    for i in range(3, len(pixels)):
        green = 1                          # starts from the first green pixel and changes the other green pixels at every 3rd number up 
        while green <= len(pixels[i]):
            if pixels[i][green] == '0':    
                print(end='')
            else:
                pixels[i][green] = 255
            green += 3
        red = len(pixels[i])-3     # changes other-colored pixel values to 0
        while red >= 0:
            pixels[i][red] = 0
            red -= 3
        blue = len(pixels[i])-1
        while blue >= 0:
            pixels[i][blue] = 0
            blue -= 3
    return pixels
            
def red(image, output, channel, lines, pixels):
    for i in range(3, len(pixels)):
        red = len(pixels[i]) -3    # starts from the red pixel at the end of list[i] and changes the other red pixels every 3rd number down
        while red >= 0:
            if pixels[i][red] == '0':
                print(end='')
            else:
                pixels[i][red] = 255
            red -= 3
        green = len(pixels[i]) -2
        while green >= 0:
            pixels[i][green] = 0
            green -= 3
        blue = len(pixels[i]) -1
        while blue >= 0:
            pixels[i][blue] = 0
            blue -= 3
    return pixels

def blue(image, output, channel, lines, pixels):
    for i in range(3, len(pixels)):
        blue = len(pixels[i]) -1
        while blue >= 0:
            if pixels[i][blue] == '0':    # if-statement checks that the string is '0'.  Another way of accessing the pixel is by casting them into integers through nested loops.  Example: for i in pixels, for j in i, pixels[i][j] = int(pixels[i][j]).  
                print(end='')
            else:
                pixels[i][blue] = 255
            blue -= 3
        red = len(pixels[i]) -3
        while red >= 0:
            pixels[i][red] = 0
            red -= 3
        green = len(pixels[i]) -2
        while green >= 0:
            pixels[i][green] = 0
            green -= 3            
    return pixels

def write(output, new_pixels):
    w = open(output, 'w')
    for i in range(0, 3):
        for j in range(0, len(new_pixels[i])):
            w.write(str(new_pixels[i][j]) + " ")
        w.write("\n")
    for l in range(3, len(new_pixels)):
        count = 0
        while count <= len(new_pixels[3]) -1:            # the writing starts from left to right for each list
            w.write(str(new_pixels[l][count]) + " ")     # nested loops are used to write 2D lists
            count += 1
        w.write("\n")         # adds a new line after every list in the 2D list

def main():
    image, output, channel, lines, pixels = template()
    if channel == ('red'):
        new_pixels = red(image, output, channel, lines, pixels)
        write(output, new_pixels)   # larger images may take time to process
    elif channel == ('green'):
        new_pixels = green(image, output, channel, lines, pixels)
        write(output, new_pixels)
    elif channel == ('blue'):
        new_pixels = blue(image, output, channel, lines, pixels)
        write(output, new_pixels)
    else:
        print(str(channel) + " isn\'t a valid channel.")    
main()