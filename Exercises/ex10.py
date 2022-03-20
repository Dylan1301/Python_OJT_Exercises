from datetime import date, timedelta

def allMonday(year = 2021):
    firstday  =date(year, 1, 1)
    firstday += timedelta(days = 7 - firstday.weekday())
    Week = firstday.isocalendar()[1]
    result = []

    while firstday.year == year:
        result.append("{} {}".format(Week, firstday))
        Week += 1
        firstday +=  timedelta(days = 7)

    return result


print(allMonday())

