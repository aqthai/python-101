#
# Author: Alvin Thai
# Description:
#     Opens, reads, and appends a file with contact information using if-statements, nested functions, while-loops, and indexing to refer to information from editable lists created by functions.
#
def main():
    print("Welcome to the contacts app!")
    names = []
    emails = []
    numbers = []
    request = ''
    f = open('contacts.txt', 'r')
    info = f.readlines()  
    if len(info) > 0:
        for line in info:          #for loop removes characters and appends data from the text file to the lists
            data = line.split(' | ')
            name = data[0]
            names.append(data[0])
            email = data[1]
            emails.append(data[1])
            number = data[2]
            numbers.append(data[2])            
    while request != 'exit':
        f = open('contacts.txt', 'r')
        info = f.readlines()          
        request = input('> ')
        info_index = -1              
        if request.startswith("show me contact"):
            name = request[16:]
            for i in range(0, len(names)):     # the for loop creates an index if the name typed in at request[16:] matches with a name from the list names
                if names[i] == name:
                    info_index = i
                    break
            if info_index != -1:
                print(name + "'s contact info:")
                print("  email: " + emails[i])
                print("  phone: " + numbers[i].strip("\n"))   # removes unecessary line
            else:
                print("Not sure who that is.")
        elif request == 'add contact':       # 'add contact' prompts 'a' mode to add information into the txt
            f = open('contacts.txt', 'a')     
            name = input("    name: ")
            email = input("    email: ")
            number = input("    phone: ")
            print("  Contact added!")
            check = False
            for n in names:             # The function in lines 46 to 51 checks to see if the input name already exists in the list called names.  If it does, then the program is prompted to do nothing.
                if n == name:
                    check = True
            if check == True:
                print("", end="")    
            else:
                if len(names) >= 1:     # If there are currently names in the list names, this if statement moves the cursor to the next line in the text document and continues appending information.
                    f.write("\n" + str(name) + " | " + str(email) + " | " + str(number))    
                    f.flush()
                    names.append(name)      # This group of appends adds input to the lists currently in the program, so that new input information is retrievable in the same run.
                    emails.append(email)
                    numbers.append(number)                     
                else:
                    f.write(str(name) + " | " + str(email) + " | " + str(number) + "\n")    # If the name does not exist in the list 'names', the input information will be added to the text file and the lists.  "\n" is added to allow the next string of information to be written on a different line.
                    f.flush()
                    names.append(name)
                    emails.append(email)
                    numbers.append(number)            
        elif request == 'exit': 
            fw = open('contacts.txt', 'w')     # Lines 66 through 69 makes sure that every line is saved into the text file.  This program does not need these lines, since 'a' mode uses the flush to save the appended information, but I used it to make sure the information saves upon exiting.
            for line in info: 
                fw.write(line)
            fw.close()              
            print("Goodbye!")
        else:
            print("Huh?")
        
main()
    
            