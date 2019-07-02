#
# Author: Alvin Thai
# Description:
#     Prints operations of a date when prompted to by text file format.  Classes are used to set attributes for date, event, and a dictionary to keep dates and events.  Methods add items to the dictionary and events to a date when prompted.
#
import sys
# Class has attributes for passed in date and event.  add_event method adds passed in event into date
class Date:
    def __init__(self, date, event):
        self._date = date
        self._event = event
    def get_date(self):
        return self._date
    def get_event(self):
        return self._event
    def set_date(self, date):
        self._date = date
    def set_event(self, event):
        self._event = event
    def __str__(self):
        return str("{}:{}".format(self._date, self._event))
    def add_event(self, occurence):
        events = []
        events.append(self._event)
        events.append(occurence)
        event = ", ".join(events)
        self._event = event
        
# Class DateSet initiates a dictionary and assignss event values to a key date 
class DateSet:
    def __init__(self, obj):
        dictionary = {}
        dictionary[obj.get_date()] = [obj.get_event()]
        self._dictionary = dictionary
    def add_date(self, obj):
        if obj.get_date() not in self._dictionary:
            self._dictionary[obj.get_date()] = [obj.get_event()]
        elif obj.get_date() in self._dictionary:
            #obj.add_event(obj.get_event())
            self._dictionary[obj.get_date()].append(obj.get_event())
    def get_dictionary(self):
        return self._dictionary
    def set_dictionary(self, dictionary):
        self._dictionary = dictionary
    def __str__(self):
        return "Dates and Events:" + self._dictionary 
                
# processes how date_str is organized, then assigns yyyy, mm, and dd to one format       
def canonicalize_date(date_str):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    if date_str.find("-") >= 0:    
        date_str = date_str.split("-")
        date_str[0] = date_str[0].lstrip(' ')
        yyyy = int(date_str[0])
        mm = int(date_str[1])
        if mm > 12:
            print("ERROR: Illegal date on line " + date_str)
            sys.exit(1)    # quits program when if-statement is qualified
        dd = int(date_str[2])
        if dd > 31:
            print("ERROR: Illegal date on line " + date_str)
            sys.exit(1)
        date = "{:d}-{:d}-{:d}".format(int(yyyy), int(mm), int(dd))
        return date
    elif date_str.find("/") >= 0:    # processing date_str if it contains '/'
        date_str = date_str.split("/")
        yyyy = int(date_str[2])
        mm = int(date_str[0])
        if mm > 12:
            print("ERROR: Illegal date on line " + date_str)
            sys.exit(1)
        dd = int(date_str[1])
        if dd > 31:
            print("ERROR: Illegal date on line " + date_str)
            sys.exit(1)
        date = "{:d}-{:d}-{:d}".format(int(yyyy), int(mm), int(dd))
        return date
    else:    # processing yyyy, mm, and dd if they were separated by spaces
        date_str = date_str.split()
        yyyy = int(date_str[2])
        for mon in range(len(months)):
            if date_str[0] == months[mon]:
                mm = int(mon+1)
        if mm > 12:
            print("ERROR: Illegal date on line " + date_str)
            sys.exit(1)
        dd = int(date_str[1])
        if dd > 31:
            print("ERROR: Illegal date on line " + date_str)
            sys.exit(1)
        date = "{:d}-{:d}-{:d}".format(int(yyyy), int(mm), int(dd))
        return date

# input file is read and processed into classes where information is organized into a data structure to be printed out when prompted
def main():
    obj2 = 0
    read = input()
    try:
        dates_and_events = open(read, 'r')
    except:
        print("ERROR: Could not open file " + filename)
    else:
        for line in dates_and_events:     # reads and edits lines so that they can be processed by the Date and DateSet classes
            line = line.strip("\n").split(":")
            if line[0].startswith('I'):
                date_str = line[0].lstrip('I ').rstrip(' ')
                event = line[1].lstrip(' ')
                if len(line) >= 3:
                    event = [line[1], line[2]]
                    event = ":".join(event)
                date = canonicalize_date(date_str)
                obj = Date(date, event)    
                if obj2 == 0:
                    obj2 = DateSet(obj)
                elif obj2 != 0:
                    obj2.add_date(obj)
            elif line[0].startswith('R'):
                date_str = line[0].lstrip('R ')
                date = canonicalize_date(date_str)
                for k, v in obj2.get_dictionary().items():
                    if k == date:
                        for i in v:  # goes through each element of the value list
                            print("{}: {}".format(k, i))
            else:
                print("ERROR: Illegal operation on line " + line)
                sys.exit(1)

main()

class DateSet:
    def __init__(self):
        read = input()
        dates = open(read, 'r')
        dictionary = {}
        for line in dates:
            line = line.strip('\n').split(':')
            if line[0].startswith('I'):
                date_str = line[0].lstrip('I ').rstrip(' ')
                event = line[1].lstrip(' ')
                if len(line) >= 3:
                    event = [line[1], line[2]]
                    event = ":".join(event)
                date = canonicalize_date(date_str)
                if date in dictionary:
                    dictionary[date].append(event)
                else:
                    dictionary[date] = [event]
            elif line[0].startswith('R'):
                date_str = line[0].lstrip('R ')
                date = canonicalize_date(date_str)
                for k, v in dictionary.items():
                    v = v.sort()
                if date in dictionary:
                    for e in dictionary[date]:
                        print("{}: {}".format(date, e))
        self._dictionary = dictionary
        
    def get_dictionary(self):
        return self._dictionary
    def set_dictionary(self, dictionary):
        self._dictionary = dictionary
    def __str__(self):
        return "Dates and Events:" + self._dictionary 

def canonicalize_date(date_str):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    if date_str.find("-") >= 0:    
        date_str = date_str.split("-")
        date_str[0] = date_str[0].lstrip(' ')
        yyyy = int(date_str[0])
        mm = int(date_str[1])
        dd = int(date_str[2])
        date = "{:d}-{:d}-{:d}".format(int(yyyy), int(mm), int(dd))
        return date
    elif date_str.find("/") >= 0:    # processing date_str if it contains '/'
        date_str = date_str.split("/")
        yyyy = int(date_str[2])
        mm = int(date_str[0])
        dd = int(date_str[1])
        date = "{:d}-{:d}-{:d}".format(int(yyyy), int(mm), int(dd))
        return date
    else:    # processing yyyy, mm, and dd if they were separated by spaces
        date_str = date_str.split()
        yyyy = int(date_str[2])
        for mon in range(len(months)):
            if date_str[0] == months[mon]:
                mm = int(mon+1)
        dd = int(date_str[1])
        date = "{:d}-{:d}-{:d}".format(int(yyyy), int(mm), int(dd))
        return date

def main():
    a = DateSet()
main()

