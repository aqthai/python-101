#
# Author: Alvin Thai
# Description:
#     Reads text file of friends, then creates nodes of those names to put in a linked list.  Name nodes are assigned friends with whoever they are connected to in a linked list assigned to each node.
#
from linked_list import *
def read():
    list_of_connections = []
    file = input('Input file: ')
    try:
        f = open(file)
        friends = f.readlines()
    except:
        print("ERROR: Could not open file" + file)
    else:
        for connection in friends:
            connection = connection.rstrip().lstrip()
            connection = connection.split()
            list_of_connections.append(connection)
        return list_of_connections

# Each person is assigned a node with linked lists of their friends.  While loops iterate through linked lists, then adds friends when they do not already exist in the list.  Names are added to the main linkedlist if they are not on it.
def social_network():
    file = read()
    main_list = LinkedList()
    current = main_list._head
    for line in file:   # connects main and friends LinkedLists
        person = Node(line[0])
        person2 = Node(line[1])
        if current == None:   # adds first node to list
            main_list.add(person)
            current = main_list._head
        while current != None:
            if current.name() == person.name():
                current.set_friends(person2)
                main_list.add(person2)
                person2.set_friends(person)
                break
            elif current._next == None and current.name() != person.name():
                main_list.add(person)
                person.set_friends(person2)
            current = current._next
        current = main_list._head
        while current != None:
            current = current._next
            
        current = main_list._head
    return main_list
        
# Reads two names, iterates through main_list to find them, then prints the names of friends they have in common.
def print_common(main_list):
    try:
        name1 = input("Name 1: ")
    except:
        print("ERROR: Unknown person " + name1)
    try:
        name2 = input("Name 2: ")
    except:
        print("ERROR: Unknown person " + name2)
    common = []
    current = main_list._head
    friends1 = ""
    friends2 = ""
    while current != None:
        if current._name == name1:
            friends1 = current._friends
        if current._name == name2:
            friends2 = current._friends
        current = current._next
    friend1 = friends1._head
    friend2 = friends2._head
    while friend1 != None:
        while friend2 != None:
            if friend1.name() == friend2.name():
                common.append(str(friend1.name()))
            friend2 = friend2._next
        friend2 = friends2._head
        friend1 = friend1._next
    if len(common) > 0:
        print("Friends in common:")
        for name in common:
            print(name)
        
def main():
    b = social_network()
    print_common(b)
main()