import calendar 
  
date = input()
def findDay(date): 
    month, day, year = (int(i) for i in date.split(' '))     
    dayNumber = calendar.weekday(year, month, day) 
    days =["Monday", "Tuesday", "Wednesday", "Thursday", 
                         "Friday", "Saturday", "Sunday"] 
    return (days[dayNumber]) 
  
# Driver program 

print(findDay(date).upper())