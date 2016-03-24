# Hint:  use Google to find python function

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'

from datetime import datetime  
d1 = datetime.strptime(date_start, '%m-%d-%Y')  
d2 = datetime.strptime(date_stop, '%m-%d-%Y')  
days = abs((d2-d1).days)  
days
####b)  
date_start = '12312013'  
date_stop = '05282015'  

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  
