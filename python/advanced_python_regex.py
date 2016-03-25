import csv
def read_data(data):
  with open(data, 'r') as f:
    data =[row for row in csv.reader(f.read().splitlines())]
  return data
  
data = Desktop/faculty.csv

fac = read_data(data)

degrees = [x[1] for x in fac]
degree_unique = set(degree)
print (degree_unique)
#8 different degrees
degrees.count('Ph.D')
degrees.count('PhD')
degrees.count('ScD')
degrees.count('Sc.D')


