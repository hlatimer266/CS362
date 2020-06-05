def is_leap_year(year):
    leap = False
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 == 0:
            leap = True
        if year % 100 != 0:
            leap = True

    return leap


def extra_days(year):
    """
    accounts for all those pesky years between epoch and
    calculated year, that should be leap years based on
    year % 4 == 0, but are NOT leap years because
    year % 100 == 0 BUT year % 400 != 0
    then add those "extra" leap days to days_remaining

    :param year: calculated year for num_sec
    :return: the number of "extra" days to account for
    years that aren't leap
    """
    test_year = 1972
    days = 0
    while test_year <= year:
        if not is_leap_year(test_year):
            days += 1
        test_year += 4

    return days


def leap_years(days_remaining):
    days_in_leap_months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    months = 0
    for m in days_in_leap_months:
        if days_remaining < m:
            break
        elif days_remaining >= m:
            days_remaining -= m
            months += 1

    return days_remaining, months


def reg_years(days_remaining):
    days_in_reg_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    months = 0
    for r in days_in_reg_months:
        if days_remaining < r:
            break
        elif days_remaining >= r:
            days_remaining -= r
            months += 1

    return days_remaining, months


def adjust_for_overflow_days(days_remaining, year):
    if is_leap_year(year):
        if days_remaining > 366:
            days_remaining -= 366
            year += 1
        if days_remaining == 366:
            days_remaining = 0
            year += 1

    if not is_leap_year(year):
        if days_remaining > 365:
            days_remaining -= 365
            year += 1
        elif days_remaining == 365:
            days_remaining = 0
            year += 1

    return days_remaining, year
