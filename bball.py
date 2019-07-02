#
# Author: Alvin Thai
# Descrpition:
#     Takes in a file with basketball game info and processes it to acquire win ratio of teams and conferences.
#
class Team:
    def __init__(self, line):
        self.file = input()
        self.a = open(self.file)
        games_info = []
        for line in self.a:
            assert len(line) == 4
            if line.startswith("#"):
                continue
            else:
                line = line.split()
                games_info.append(line)
    def name(self):
        self.name = name
    def conf(self):
        self.conf = conf
    def win_ratio(self):
        self.win_ratio = win_ratio
    def __str__(self):
        win_ratio_str = str(win_ratio)
        return "{} : {}".format(name, win_ratio_str) 
    
class Conference:
    def __init__(self, conf):
        self.conf = conf
        teams = []
    def __contains(self, team):
        return team in teams
    def name(self):
        return self.conf
    def add(self, team):
        teams.append(team)
    def win_ratio_avg(self):
        win_ratio = win/(wins + loses)
        return win_ratio
    def __str__(self):
        win_ratio_str = str(win_ratio)
        return "{} : {}".format(name, win_ratio_str) 

class ConferenceSet:
    def __init__(self):
        set_of_conf = []
    def add(self, team):
        teams.append(team)
    def best(self):
        M = 0
        
        
    