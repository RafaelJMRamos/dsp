#q1
import csv
def read_data(data):
  with open(data, 'r') as f:
    data =[row for row in csv.reader(f.read().splitlines())]
  return data
  
data = Desktop/faculty.csv

fac = read_data(data)

degrees = [x[1] for x in fac]
no_periods= [x.replace('.','') for x in degrees]
no_space= [x.replace(' ','') for x in no_periods]
degree_unique = set(no_space[1:])
print (degree_unique)
#8 different degrees
no_space.count('PhD')
no_space.count('PhDScD')
no_space.count('ScD')
no_space.count('MDMPHPhD')
no_space.count('BSEdMSPhD')
no_space.count('JDMAMPHMSPhD')

#q2
titles = [x[2] for x in fac]
title_unique = set(titles[1:])
titles.count('Associate Professor of Biostatistics')
titles.count('Assistant Professor of Biostatistics')
titles.count('Professor of Biostatistics')

#q3
emails = [x[3] for x in fac]  
headerless_emails=emails[1:]  
print(headerless_emails)

#q4
domains = [x.split('@',2)[-1] for x in emails]
uniquedomains=list(set(domains[1:]))



