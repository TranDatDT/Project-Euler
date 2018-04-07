'''
You are given the following information, but you may prefer to do some
research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century
    unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?
'''


def is_leap(n):
    if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
        return True

    return False


day = 31
month = 12
year = 1899

count = 0

while year < 2001:
    day = day + 7

    if month == 2:
        if is_leap(year):
            if day > 29:
                day -= 29
                month += 1
                if month == 12:
                    month = 1

        else:
            if day > 28:
                day -= 28
                month += 1

    elif month == 4 or month == 6 or month == 9 or month == 11:
        if day > 30:
            day -= 30
            month += 1
    else:
        if day > 31:
            day -= 31
            month += 1

    if month == 13:
        month = 1
        year += 1

    if day == 1:
        count += 1
        if year == 1900:
            count -= 1

print(count)
