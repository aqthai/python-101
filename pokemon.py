#
# Author: Alvin Thai
# Description:
#     Imports a csv file with pokemon information and adds it into a 2-level dictionary, calculates the average stat values for each type to make another dictionary, finds the type with the highest max value for each stat, and prints the type with the max average value when the user types the stat in the query.
# 
import csv
# Arranges data from import csv file into 2-level dictionary
def init():
    pokemons = {}
    stats = []
    values = []
    filename = input()
    f = open(filename, 'r')
    data = csv.reader(f)
    for line in data:
        if not line[2] in pokemons and '#' not in line:
            pokemons[line[2]] = {line[1]: (line[4], line[5], line[6], line[7],
                                           line[8], line[9], line[10])}
        elif line[2] in pokemons and line[1] not in pokemons[line[2]] and '#' not in line:
            pokemons[line[2]][line[1]] = (line[4], line[5], line[6], line[7],
                                          line[8], line[9], line[10])
    return pokemons

# Calculates the average stats of each type and creates a dictionary with the types as keys and the average stats as values
def type_averages_dict(pokemons):
    types_dict = {}
    sum_total = 0
    sum_hp = 0
    sum_atk = 0
    sum_def = 0
    sum_spatk = 0
    sum_spdef = 0
    sum_speed = 0
    for types in pokemons:
        types_dict[types] = 0
        for name in pokemons[types]:
            stat = pokemons[types][name]
            sum_total += int(stat[0])
            sum_hp += int(stat[1])
            sum_atk += int(stat[2])
            sum_def += int(stat[3])
            sum_spatk += int(stat[4])
            sum_spdef += int(stat[5])
            sum_speed += int(stat[6])
        types_dict[types] = (sum_total/len(pokemons[types]),
                             sum_hp/len(pokemons[types]),
                             sum_atk/len(pokemons[types]),
                             sum_def/len(pokemons[types]),
                             sum_spatk/len(pokemons[types]),
                             sum_spdef/len(pokemons[types]),
                             sum_speed/len(pokemons[types]))
        sum_total = 0
        sum_hp = 0
        sum_atk = 0
        sum_def = 0
        sum_spatk = 0
        sum_spdef = 0
        sum_speed = 0
    return types_dict

# Finds the type with the highest average of each stat and makes a dictionary with the stats as keys and the type as values.  A 2d-list was used to store the stat values of each type 
def max_avg_values(types_dict):
    totals = []
    hp = []
    atk = []
    defense = []
    sp_atk = []
    sp_def = []
    speed = []
    stat_list = []
    max_avg_values = []
    stat_names = ["total", "hp", "attack", "defense", "specialattack", "specialdefense", "speed"]
    dictionary = {}
    for types in types_dict:
        stat = types_dict[types]
        totals.append(stat[0])
        hp.append(stat[1])
        atk.append(stat[2])
        defense.append(stat[3])
        sp_atk.append(stat[4])
        sp_def.append(stat[5])
        speed.append(stat[6])
    stat_list.append(totals)
    stat_list.append(hp)
    stat_list.append(atk)
    stat_list.append(defense)
    stat_list.append(sp_atk)
    stat_list.append(sp_def)
    stat_list.append(speed)
    max_avg_values.append(max(totals))
    max_avg_values.append(max(hp))
    max_avg_values.append(max(atk))
    max_avg_values.append(max(defense))
    max_avg_values.append(max(sp_atk))
    max_avg_values.append(max(sp_def))
    max_avg_values.append(max(speed))
    n = 0
    for i in stat_names:
        dictionary[i] = n
        n += 1
    for k, v in dictionary.items():
        dictionary[k] = max_avg_values[v]
    for k, v in dictionary.items():
        for types, avg in types_dict.items():
            if v in avg:
                dictionary[k] = types
    return dictionary, max_avg_values

# the input function in this while loop takes a query stat and prints the pokemon type with the highest average stat value
def query(dictionary, max_avg_values):
    while True:
        query = input()
        query = query.lower()        
        if query == "total":
            print("{}: {}".format(dictionary['total'], max_avg_values[0]))
        elif query == "hp":
            print("{}: {}".format(dictionary['hp'], max_avg_values[1]))
        elif query == "attack":
            print("{}: {}".format(dictionary['attack'], max_avg_values[2]))
        elif query == "defense":
            print("{}: {}".format(dictionary['defense'], max_avg_values[3]))
        elif query == "specialattack":
            print("{}: {}".format(dictionary['specialattack'], max_avg_values[4]))
        elif query == "specialdefense":
            print("{}: {}".format(dictionary['specialdefense'], max_avg_values[5]))        
        elif query == "speed":
            print("{}: {}".format(dictionary['speed'], max_avg_values[6]))
        elif query == "":
            break
    
def main():
    a = init()
    b = type_averages_dict(a)
    c, d = max_avg_values(b)
    query(c, d)
main()
    