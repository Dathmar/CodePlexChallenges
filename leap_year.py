def is_leap_year(year):
    if (year % 100 == 0 and year % 400 != 0) or year % 4 != 0:
        return false
    elif year % 4 == 0:
        return true

print(is_leap_year(800))