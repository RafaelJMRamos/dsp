#removing header
emails = emails [:1]

csvfile = 'emails.csv'
with open(csvfile, 'w') as output:
  writer=csv.writer(output, lineterminator='\n')
  for val in emails:
    writer.writerow([val])
