#
# Author: Alvin Thai
# Description:
#     Reads a csv file with species names and the parks they live at, creates a dictionary with each park as the keys and the species living in them as values, then prints the species that are found in the largest number of parks.  The program uses asserts to check for correct structure types and if structures are usable.
#
# Reads csv file, converts each line into a list, and takes park and species name to create a dictionary.  Asserts check if preceding methods worked and if proper information type is extracted from the file.
def init():
    parks = {}
    species = []
    sinfo = input()
    s = open(sinfo, 'r')
    data = s.readlines()
    for line in data:
        line = line.rstrip('\n').split(",")    # breaks strings into lists.  Line has to be a list in order for the function to continue 
        assert type(line) == list and len(line) >= 0   # checks that line in data are lists before undergoing if-statements
        if line[0] not in parks and "#" not in line[0]:
            parks[line[0]] = species
            species = []
            assert type(line[2]) == str   # checks if the element on line[2] is a string before adding to dictionary
            parks[line[0]].append(line[2])
        elif line[0] in parks:
            assert line[0].startswith("#") == False
            parks[line[0]].append(line[2])
    s.close()        
    return parks

# Takes a dictionary as a parameter, then makes another dictionary with species names and the number of parks they live in.  To make sure the computation in the nested for-loop is done correctly, an assert checks that an integer is assigned to each value of count_dict.
def count(parks):
    assert len(parks) != 0 and type(parks) == dict   # checks if the argument type is a dictionary
    count_dict = {}
    species_names = []
    number_of_parks = 0
    for park in parks:
        for species_name in parks[park]:
            if species_name not in count_dict:
                count_dict[species_name] = 1
            elif species_name in count_dict:
                count_dict[species_name] += 1
            assert type(count_dict[species_name]) == int # checks that an integer is assigned to each value of count_dict
    for v in count_dict.values():
        if v >= number_of_parks:
            number_of_parks = v
            assert type(number_of_parks) == int
    for k, v in count_dict.items():
        if v == number_of_parks:
            species_names.append(k)
            assert len(species_names) > 0   # will stop the program if there are no species with the number of parks they occur in
    for species_name in species_names:
        species_name = species_name.lower()
        print("{} -- {:d} parks".format(species_name, number_of_parks))     
    
def main():
    a = init()
    assert type(a) == dict
    count(a)
main()
    