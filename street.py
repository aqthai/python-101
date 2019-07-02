#
# Author: Alvin Thai
# Description: 
#     Recursion function that builds a street image.
#
class Building:
    def __init__(self, width, height, brick):
        self._width = int(width)
        self._height = int(height)
        self._brick = brick
    def at_height(self, height):
        if height >= self._height:  # attributes are NoneType until casted
            print(self._width * " ")
        else:
            print((self._brick) * int(self._width))

class Park:
    def __init__(self, width, foliage):
        self._width = int(width)
        self._foliage = foliage
    def at_height(self, height):
        if height >= 5:
            print(self._width * " ")
        elif height == 4:
            print(" " * (self._width - 5)/2 + "  " + self._foliage + "  " + " " * (self._width - 5)/2)
        elif height == 3:
            print(" " * (self._width - 5)/2 + " " + self._foliage * 3 + " " + " " * (self._width - 5)/2)        
        elif height == 2:
            print(" " * (self._width - 5)/2 + self._foliage * 5 + " " * (self._width - 5)/2)
        elif height == 1 or height == 0:
            print(" " * (self._width - 1)/2 + "|" + " " * (self._width - 1)/2)
        
class EmptyLot:
    def __init__(self, width, trash):
        self._width = int(width)
        self._trash = str(trash)
    def at_height(self, height):
        if height >= 1:
            print(" " * self._width)
        elif self._width <= len(self._trash):
            print(str(self._trash[:self._width]).replace("_", " "))
        elif self._width > len(self._trash):
            print(str(self._trash).replace("_", " ") + self.at_height(0))
            self._width -= len(self._trash)
            
# s is a list of objects.  An input is put in the parameter and processed 
def make_s(park):
    park_pieces = park.split()
    s = []
    if park_pieces == []:
        return s
    elif park_pieces[0].startswith("b"):
        b = Building(park_pieces[0][2], park_pieces[0][4], park_pieces[0][6])
        s.append(b)
        return s + make_s("".join(park_pieces[1:]))
    elif park_pieces[0].startswith("p"):
        p = Park(park_pieces[0][2:])
        s.append(p)
        return s + make_s("".join(park_pieces[1:]))
    elif park_pieces[0].startswith("e"):
        e = EmptyLot(park_pieces[0][2], park_pieces[0][4:])
        s.append(e)
        return s + make_s("".join(park_pieces[1:]))
    
# Prints strings out of each element of s at every height
def print_street_at_height(s, h):
    if s == []:
        str(s[0].at_height(h)) + str(print_street_at_height(s[1:], h-1))
    else:
        str(s[0].at_height(h)) + str(print_street_at_height(s[1:], h))
        
def main():
    park = input("Street: ")
    s = make_s(park)
    print_street_at_height(s, 3)
main()