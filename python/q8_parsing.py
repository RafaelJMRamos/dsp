#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.


import csv

def read_data(data):    
  with open(data, 'r') as f:
    data = [row for row in csv.reader(f.read().splitlines())]
  return data

data = footall.csv    
    

def get_min_score_difference(self, parsed_data):
  parsed_data.pop(0)
  goals = [x[5] for x in parsed_data]
  goals_allowed = [x[6] for x in parsed_data]
  return min([float(x) - float(y) for x, y in zip(goals, goals_allowed)])


def get_team(self, index_value, parsed_data):
  teams = [x[0] for x in parsed_data]
  return teams[index_value]
