#
# Author: Alvin Thai
# Description:
#     Reads csv files about parks and number of flora and fauna in each park, creates a dictionary with park names and their areas and a dictionary with the number of flora and fauna in each park, then prints the density of flora and fauna in each park.  Assertions are used to check if file inputs are usable.
#
# Reads a csv file with parks and their areas and creates a dictionary with each park as keys and the areas as values.  Values are stored as single element tuples.  The dictionary is returned for later use.
def init():
    parks = {}
    pfile = input()
    p = open(pfile, 'r')
    park = p.readlines()
    for line in park:
        line = line.rstrip('\n').split(",")
        assert type(line) == list  # checks that a list is created from line
        if "#" not in line[0]:
            parks[line[0]] = tuple([int(line[2])])
    p.close()
    return parks

# Reads a file with species in each park, then counts the number of flora and fauna in each park.  Creates a dictionary with each park as the keys and the flora/ fauna counts as values in tuples.  Asserts are used to check if the file has proper info.  
def species_init(parks):
    assert type(parks) == dict  # the argument has to be a dictionary 
    categories = {}
    c_flora = ['Algae', 'Fungi', 'Nonvascular Plant', 'Vascular Plant']
    c_fauna = ['Amphibian', 'Bird', 'Crab/Lobster/Shrimp', 'Fish', 'Insect',\
             'Invertebrate', 'Mammal', 'Reptile', 'Slug/Snail',\
             'Spider/Scorpion']
    flora = 0
    fauna = 0
    sinfo = input()
    s = open(sinfo, 'r')
    species = s.readlines()
    for line in species:
        line = line.rstrip('\n').split(",")
        assert line[1] in c_flora or c_fauna  # the file has to have the categories indicated in the lists or it will not run
        if "#" not in line[0] and line[0] not in categories:
            categories[line[0]] = tuple([flora, fauna])    # park names are established to keys of this dictionary
    for park in categories:
        for line in species:    # increases the count of flora and fauna for each line[1] read through
            line = line.rstrip('\n').split(",")
            if line[1] in c_flora and line[0] == park and "#" not in line[0]:
                flora += 1
            if line[1] in c_fauna and line[0] == park and "#" not in line[0]:
                fauna += 1
        categories[park] = tuple([flora, fauna])
        flora = 0
        fauna = 0
    s.close()
    return parks, categories

# Reads both dictionaries as the argument, calculates the density of flora and fauna in each park, then prints them.  If the dictionary created from the species file does not have information about the parks in the parks, it will say "no data available"         
def print_density(parks, categories):
    assert type(parks) == dict and type(categories) == dict
    for park in categories:
        assert type(categories[park]) == tuple        # values of categories and parks need to be tuples 
        for area in parks:
            assert type(parks[area]) == tuple
            if park == area:
                park_name = park
                assert type(categories[park][0]) == int \
                and type(categories[park][1]) == int   # elements of the tuple values in categories need to be integers
                flora_per_acre = categories[park][0] / parks[area][0] 
                fauna_per_acre = categories[park][1] / parks[area][0] 
                print("{} -- flora: {:f} per acre; fauna: {:f} per acre".format(park_name, flora_per_acre, fauna_per_acre))
    for area in parks:
        if area not in categories:    # indicates if a park in the park file is missing from the parks in the species file
            park_name = area
            print("{} -- no data available".format(park_name)) 
            
def main():
    a = init()
    a, b = species_init(a)
    assert type(a) == dict and type(b) == dict
    print_density(a, b)
main()