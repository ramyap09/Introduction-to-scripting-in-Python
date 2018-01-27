"""
Project for Week 4 of "Python Programming Essentials".
Collection of functions to process dates.
"""

import datetime

def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    if month == 12:
        return 31
    else:
        date1 = datetime.date(year,month,1)
        date2 = datetime.date(year,month+1,1)
        diff = date2-date1
        return diff.days



def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    if year < datetime.MINYEAR or year > datetime.MAXYEAR or month < 1 or month > 12 :
        return False
    else:
        days = days_in_month(year, month)
        if day >= 1 and day <= days :
            return True
        else:
            return False



def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """
    if is_valid_date(year1, month1, day1) and is_valid_date(year2, month2, day2) :
        date_earlier = datetime.date(year1, month1, day1)
        date_later = datetime.date(year2, month2, day2)
        if date_earlier > date_later :
            return 0
        else:
            diff = date_later - date_earlier
            return diff.days
    else:
        return 0




def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input
      date is in the future.
    """
    today_date = datetime.date.today()
    if is_valid_date(year, month, day) :
        bday = datetime.date(year, month, day)
    else:
        return 0
    if bday > today_date:
        return 0
    else:
        age = days_between(year, month, day, today_date.year, today_date.month,today_date.day)
        return age

print(age_in_days(0, 1, 21))
