import time
from datetime import datetime
from pytz import timezone



fmt = "%m-%d %H:%M:%S"
now_utc = datetime.now(timezone('UTC'))
now_pacific = now_utc.astimezone(timezone('US/Pacific'))   


on2Min = 120
on5Min = 300
on3Min = 180
Sleep24Hours = 86400 
SleepHour = 3600
Sleep6Hours= 21600
Sleep12Hours= 43200

print (now_pacific.strftime(fmt))
