#
# Author: Alvin Thai
# Description:
#     Reads the titles of fake news, extracts the words, and sets a count of how many times each word appears.  Node and LinkedList classes are used to form the list of words in descending order by how many times the words of the titles appear.
#
import csv
import string
import sys
csv.field_size_limit(sys.maxsize)   # allows larger files to be read
class Node:
    def __init__(self, word):
        self._word = word
        self._count = 1
        self._next = None
    def word(self):
        return self._word
    def count(self):
        return self._count
    def next(self):
        return self._next
    def set_next(self, target):
        self._next = target
    def incr(self):
        self._count += 1
    def __str__(self):
        return str(self._word) + " : " + str(self._count) + "; "
    
class LinkedList:
    def __init__(self):
        self._head = None
    def is_empty(self):
        return self._head == None
    def is_in(self, word):    # checks if word is in LinkedList and returns True if so
        ptrhead = self._head
        while ptrhead != None:
            if ptrhead.word() == word:
                return True
            ptrhead = ptrhead._next
        return False
# based on short assignment
    def head(self):
        return head._next
    def update_count(self, word):
        ptrhead = self._head
        if self.is_in(word):       #  Increments count if word is in LinkedList
            while ptrhead != None:
                if ptrhead.word() == word:
                    ptrhead.incr()
                ptrhead = ptrhead._next
        else:                      # adds node if not
            w = Node(word)
            self.add(w)

# based on short assignment
    def add(self, node):
        node._next = self._head
        self._head = node
# based on short assignment
    def rm_from_hd(self):
        _node = self._head
        self._head = _node._next
        _node._next = None
        return _node
# based on short assignment
    def insert_after(self, node1, node2):
        node2._next = node1._next
        node1._next = node2
# based on short assignment
    def sort(self):
        descending = LinkedList()
        if self._head != None:
            curr_word = self.rm_from_hd()
            descending.add(curr_word)
        while self._head != None:
            curr_word = self.rm_from_hd()
            ptrhead = descending._head
            while curr_word.count() <= ptrhead.count() and ptrhead._next != None:
                ptrhead = ptrhead._next
            if curr_word.count() > ptrhead.count():
                descending.add(curr_element)
            elif curr_word.count() < ptrhead.count() and ptrhead._next == None:
                ptrhead._next = curr_word
            elif ptrhead._next.count() < curr_word.count() <= ptrhead.count():
                descending.insert(ptrhead, curr_word)
        self._head = descending._head
        return self
    def get_nth_highest_count(self, n):
        ptrhead = self._head
        while n >= 0:
            ptrhead = self._next
            n -= 1
        return ptrhead.count()
    def print_upto_count(self, n):
        ptrhead = self._head
        while ptrhead._head != None:
            if ptrhead.count() >= n:
                print("{} : {:d}".format(ptrhead.word(), ptrhead.count()))
            ptrhead = ptrhead._next
    def __str__(self):
        lst = 'List[ '
        curr_node = self._head
        while curr_node != None:
            lst += str(curr_node)
            curr_node = curr_node._next
        lst += ']'
        return lst

def read():
    infile = input('File: ')
    file = open(infile, encoding='utf8')
    csvreader = csv.reader(file)
    titles_read = []
    words = []
    for itemlist in csvreader:
        titles_read.append(itemlist[4])
    for title in titles_read:
        for i in string.punctuation:
            title = title.replace(i, " ")
        title = title.split()
        for l in title:
            if len(l) >= 3:
                words.append(l.lower())
    return words

def read_N(words):
    n = input('N: ')

def main():
    words = read()
    words.remove(words[0])
    obj = LinkedList()
    element = Node(words[0])
    obj.add(element)
    words.remove(words[0])
    point = obj._head
    for word in words:
        obj.update_count(word)
    obj.sort()
    print(obj)
main()
