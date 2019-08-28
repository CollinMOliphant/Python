import time
from datetime import datetime
from pytz import timezone



fmt = "%m-%d %H:%M"
now_utc = datetime.now(timezone('UTC'))
now_pacific = now_utc.astimezone(timezone('US/Pacific'))   

Fertilzer_pump = 17
water_value = 23
current_day = 1
days_running = 14
pinList = [23, 17]

on10sec = 10
on1Min = 60
on2Min = 120
on5Min = 300
on3Min = 180
Sleep24Hours = 86400 
SleepHour = 3600
Sleep6Hours= 21600
Sleep12Hours= 43200
Sleep24Hours=86400

waterONtime = int(on3Min  /  60)


print ".=======================."
print "Date started:"+ (now_pacific.strftime(fmt))
print ".=======================."
print ""
print "Day " + str(current_day)
print "Watering for " +  str(waterONtime) + " Minutes"
print "........................"
print "Valve open, wait 10 sec"
#GPIO.output(24, 0)
time.sleep(on10sec)
print "Pump on"
#GPIO.output(17, 0)
while (waterONtime > 0):
    print (str(waterONtime) + " min left")
    time.sleep(on1Min)
    waterONtime = waterONtime - 1
#GPIO.output(24, 1)
#GPIO.output(17, 1)
#GPIO.cleanup()
print "________________________"
print ""
print "Off for 24 hours"
print ""
#time.sleep(Sleep24Hours)
print "________________________"
print ""
print "Day" + " " + str(current_day)
print "Turned off"
print "________________________"

