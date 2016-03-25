import csv
def read_data(data):
  with open(data, 'r') as f:
    data =[row for row in csv.reader(f.read().splitlines())]
  return data
  
data = Desktop/faculty.csv

fac = read_data(data)

degrees = [x[1] for x in fac]
degree_unique = set(degree[1:])
print (degree_unique)
#8 different degrees
degrees.count('Ph.D')
degrees.count('PhD')
degrees.count('ScD')
degrees.count('Sc.D')

titles = [x[2] for x in fac]
title_unique = set(titles[1:])
titles.count('Associate Professor of Biostatistics')
titles.count('Assistant Professor of Biostatistics')
titles.count('Professor of Biostatistics')

emails = [x[3] for x in fac]  
headerless_emails=emails[1:]  
print(headerless_emails)

domains = [x.split('@',2)[-1] for x in emails]
uniquedomains=list(set(domains[1:]))



