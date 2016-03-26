#q6

def read_data(data):
  with open(data, 'r') as f:
    data =[row for row in csv.reader(f.read().splitlines())]
  return data
  
data = Desktop/faculty.csv

fac = read_data(data)
fac = fac[1:]
nonames = [x[1:] for x in fac]
names = [x[0] for x in fac]
lastname = [x.split(' ')[-1] for x in names]

tuplast = tuple(lastname)
from collections import defaultdict
faculty_dict =defaultdict(list)

for i,j in zip(tuplast,nonames):
  faculty_dict[i].append(j)
print (faculty_dict)  
#q7
firstname = [x.split(' ')[0] for x in names]
newname = list(zip(firstname,lastname))
professor_dict = dict(zip(newname,nonames))
print (professor_dict)
#q8
order = sorted(professor_dict, key = lambda x:x[1])
for key in order:
  print(key, professor_dict[key])



