from datetime import datetime, timedelta
import pytz

timezone = pytz.timezone("Asia/Bangkok")

current_date = datetime.now(tz = timezone)

weekday = current_date.weekday()

if weekday < 5:
    last_friday = current_date - timedelta(days=3 + weekday)
else:
    last_friday = current_date - timedelta(days = weekday - 4)
print(last_friday)