# Take the inputs
from datetime import *
year = int(input("Enter your birth year in numbers eg. 1872: "))
month = int(input("Enter birth month(ex. 1): "))
birthDate = int(input("Enter the date of birth eg. 23: "))
gender_input = input("Gender(ex.Male or Female): ")

anshanti = date(year, month, birthDate)

dayFinal = anshanti.strftime("%A")

# # change the year string into integer and keep only the last two integers
# YY = int(year[-2:])
# yearCode = (YY+(YY // 4)) % 7


# # Extract the century code from the year entered
# CC = int(year[:2])
# centuryCode = 0
# if CC == 17:
#     centuryCode = 4
# elif CC == 18:
#     centuryCode = 2
# elif CC == 19:
#     centuryCode = 0
# elif CC == 20:
#     centuryCode = 6
# elif CC == 21:
#     centuryCode = 4
# elif CC == 22:
#     centuryCode = 2
# elif CC == 23:
#     centuryCode = 0

# # month code output
# month_code = 0

# if month == "January":
#     month_code = 0
# elif month == "February":
#     month_code = 3
# elif month == "March":
#     month_code = 3
# elif month == "April":
#     month_code = 6
# elif month == "May":
#     month_code = 1
# elif month == "June":
#     month_code = 4
# elif month == "July":
#     month_code = 6
# elif month == "August":
#     month_code = 2
# elif month == "September":
#     month_code = 5
# elif month == "October":
#     month_code = 0
# elif month == "November":
#     month_code = 3
# elif month == "December":
#     month_code = 5
# else:
#     print("write correctly and start with a capital letter {month_code}")


# # leap year code
# leapYearCode = 0
# if YY % 4 == 0:
#     leapYearCode = 1
# elif YY % 4 != 0:
#     leapYearCode = 0


# day1 = yearCode + month_code + centuryCode + birthDate - leapYearCode
# dayFinal = day1 % 7

# Ashanti names
if dayFinal == "Sunday" and gender_input == "Male":
    print("your anshanti name is KWASI")
elif dayFinal == "Sunday" and gender_input == "Female":
    print("your anshanti name is AKOSUA")
elif dayFinal == "Monday" and gender_input == "Male":
    print("your anshanti name is KODJO")
elif dayFinal == "Monday" and gender_input == "Female":
    print("your anshanti name is ADJOA")
elif dayFinal == "Tuesday" and gender_input == "Male":
    print("your anshanti name is KWABENA ")
elif dayFinal == "Tuesday" and gender_input == "Female":
    print("your anshantin name is ABENAA")
elif dayFinal == "Wednesday" and gender_input == "Male":
    print("your anshanti name is KWAKU")
elif dayFinal == "Wednesday" and gender_input == "Female":
    print("your anshanti name is AKUA")
elif dayFinal == "Thursday" and gender_input == "Male":
    print("your anshanti name is YAW")
elif dayFinal == "Thursday" and gender_input == "Female":
    print("your anshanti name is YAA")
elif dayFinal == "Friday" and gender_input == "Male":
    print("your anshanti name is KOFI")
elif dayFinal == "Friday" and gender_input == "Female":
    print("your anshanti name is AFIA")
elif dayFinal == "Saturday" and gender_input == "Male":
    print("your anshanti name is KWAME")
elif dayFinal == "Saturday" and gender_input == "Female":
    print("your anshanti name is AMMA")
else:
    print("ERROR!!!")
# print(dayFinal)
