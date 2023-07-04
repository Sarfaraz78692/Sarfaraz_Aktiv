#Write a Python program to calculate the number of days between two dates.

from datetime import date
 
 
def numOfDays(date1, date2):
    return (date2-date1).days
 

date1 = date(2018, 11, 10)
date2 = date(2018, 12, 25)
print(numOfDays(date1,date2))
        
        
