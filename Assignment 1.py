

import calendar

cur_year = 2017

date = input("Enter birth date (1-31)\n")

endings = ["st", "nd", "rd"]+ 17*["th"] + ["st", "nd", "rd"] + 7*["th"] + ["st"]

days = ['Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday']

month = int(input("Enter month you were born in(1-12)\n"))

month_names = ['January','February',
               'March',
                'April',
               'May','June',
                'July','August',
               'September',
                'October','November',
               'December']

age = int(input("How old are you now? \n"))

a = month_names[month-1]
b = int(date)
c = (cur_year-age)
d = date+endings[a-1]
e = calendar.weekday(c,month,b)
f = days[e]

print("You were born on",f ,d, a,"of the year " ,c)
