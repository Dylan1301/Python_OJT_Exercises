import datetime
import pytz

#Define the timezone
timezone = pytz.timezone("Asia/Bangkok")

# Current date and time
date = datetime.datetime.now(tz = timezone)

# Current Year
year = date.year

# Current Month of Year
month = date.month

# Current week of the year

weekofyear = date.isocalendar()[1]

# Current week day of the week

weekday = date.weekday()

# Current day of year
dayofyear = date.timetuple().tm_yday

# Current day of the month
dayofmonth = date.timetuple().tm_mday
# or just get current date


# Current Week day
dayofweek = date.timetuple().tm_wday


# Convert String to date

dateString = "Mar 17 2022 7:45AM"
dateConversion = datetime.datetime.strptime(dateString,"%b %d %Y %I:%M%p")
print(dateConversion)