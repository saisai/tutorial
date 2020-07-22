
import datetime

print(dir(datetime))

dd = [d  for d in dir(datetime)]
for d in dd:
    print(d)
    
print(datetime.MINYEAR)

print(datetime.MAXYEAR)

print(datetime.date)
print(datetime.date.today())
print(datetime.date.today().year)
print(datetime.date.today().month)

print(datetime.date(2000, 4, 29))


print(datetime.time())
print(datetime.time(hour=23, minute=59, second=59))
print(datetime.time(hour=23, minute=59, second=59, microsecond=234566))

#datetime(year, month, day)
a = datetime.datetime(2018, 11, 28)
print(a)

# datetime(year, month, day, hour, minute, second, microsecond)
b = datetime.datetime(2017, 11, 28, 23, 55, 59, 342380)
print(b)



from datetime import datetime

a = datetime(2017, 11, 28, 23, 55, 59, 342380)
print("year =", a.year)
print("month =", a.month)
print("hour =", a.hour)
print("minute =", a.minute)
print("timestamp =", a.timestamp())


#Difference between two dates and times

from datetime import datetime, date

t1 = date(year = 2018, month = 7, day = 12)
t2 = date(year = 2017, month = 12, day = 23)
t3 = t1 - t2
print("t3 =", t3)

t4 = datetime(year = 2018, month = 7, day = 12, hour = 7, minute = 9, second = 33)
t5 = datetime(year = 2019, month = 6, day = 10, hour = 5, minute = 55, second = 13)
t6 = t4 - t5
print("t6 =", t6)

print("type of t3 =", type(t3)) 
print("type of t6 =", type(t6))  

# Difference between two timedelta objects

from datetime import timedelta

t1 = timedelta(weeks = 2, days = 5, hours = 1, seconds = 33)
t2 = timedelta(days = 4, hours = 11, minutes = 4, seconds = 54)
t3 = t1 - t2

print("t3 =", t3)


# Example 13: Printing negative timedelta object

from datetime import timedelta

t1 = timedelta(seconds = 33)
t2 = timedelta(seconds = 54)
t3 = t1 - t2

print("t3 =", t3)
print("t3 =", abs(t3))

# Example 14: Time duration in seconds

from datetime import timedelta

t = timedelta(days = 5, hours = 1, seconds = 33, microseconds = 233423)
print("total seconds =", t.total_seconds())

'''
Python format datetime
The way date and time is represented may be different in different places, organizations etc. It's more common to use mm/dd/yyyy in the US, whereas dd/mm/yyyy is more common in the UK.

Python has strftime() and strptime() methods to handle this.

Python strftime() - datetime object to string
The strftime() method is defined under classes date, datetime and time. The method creates a formatted string from a given date, datetime or time object.

Example 15: Format date using strftime()

Here, %Y, %m, %d, %H etc. are format codes. The strftime() method takes one or more format codes and returns a formatted string based on it.

In the above program, t, s1 and s2 are strings.

%Y - year [0001,..., 2018, 2019,..., 9999]
%m - month [01, 02, ..., 11, 12]
%d - day [01, 02, ..., 30, 31]
%H - hour [00, 01, ..., 22, 23
%M - minute [00, 01, ..., 58, 59]
%S - second [00, 01, ..., 58, 59]
'''


from datetime import datetime

# current date and time
now = datetime.now()

t = now.strftime("%H:%M:%S")
print("time:", t)

s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("s1:", s1)

s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("s2:", s2)

'''
Python strptime() - string to datetime
The strptime() method creates a datetime object from a given string (representing date and time).

Example 16: strptime()
'''

from datetime import datetime

date_string = "21 June, 2018"
print("date_string =", date_string)

date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)



from datetime import datetime
import pytz

local = datetime.now()
print("Local:", local.strftime("%m/%d/%Y, %H:%M:%S"))


tz_NY = pytz.timezone('Asia/Bangkok') 
datetime_NY = datetime.now(tz_NY)
print("Bangkok:", datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))

tz_NY = pytz.timezone('Asia/Yangon') 
datetime_NY = datetime.now(tz_NY)
print("Yangon:", datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))

tz_NY = pytz.timezone('America/New_York') 
datetime_NY = datetime.now(tz_NY)
print("NY:", datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))

tz_London = pytz.timezone('Europe/London')
datetime_London = datetime.now(tz_London)
print("London:", datetime_London.strftime("%m/%d/%Y, %H:%M:%S"))

# https://www.programiz.com/python-programming/datetime