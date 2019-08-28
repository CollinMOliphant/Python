import RPi.GPIO as GPIO
import time  
from datetime import datetime
from pytz import timezone

GPIO.setmode(GPIO.BCM)

fmt = "%m-%d %H:%M"
now_utc = datetime.now(timezone('UTC'))
now_pacific = now_utc.astimezone(timezone('US/Pacific'))   

Fertilzer_pump = 17
water_value = 23
current_day = 1
days_running = 14
pinList = [23, 17, 24]
  
on10sec = 10
on1Min = 60
on2Min = 120
on5Min = 300
on10Min = 600
on3Min = 180
Sleep24Hours = 86400
SleepHour = 3600
Sleep6Hours= 21600
Sleep12Hours= 43200
Sleep24Hours=86400

waterONtime = int(on3Min  /  60)
fertONtime = int(on10Min  /  60)

waterCounter = waterONtime
fertCounter = fertONtime

#1 monday | fert
#2 tue
#3 wed    | fert
#4 thur
#5 friday | water
#6 sat
#7 sun    | fert

  
for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)
  
try:
    while current_day <= days_running: 

        #Initializes and sets start date
        if current_day == 1:
            print ".=======================."
            print "Date started:"+ (now_pacific.strftime(fmt))
            print ".=======================."
            print ""
            print "Day " + str(current_day)
            print "Fert for " +  str(fertONtime) + " Minutes"
            print "........................"
            print "Valve open, wait 10 sec"
            GPIO.output(24, 0)
            time.sleep(on10sec)
            print "Pump on"
            GPIO.output(17, 0)
            while (fertCounter > 0):
                print (str(fertCounter) + " min left")
                time.sleep(on1Min)
                fertCounter = fertCounter - 1
            GPIO.output(24, 1)
            GPIO.output(17, 1)
            print ""
            print "Completed"
            print ""
            print "--------------------------"
            time.sleep(Sleep24Hours)

        #off on day 2,4,6
        if current_day == 2 or current_day == 4 or current_day == 6:
            print ""
            print "Day" + " " + str(current_day)
            print "Turned off"
            print ""
            print "--------------------------"
            time.sleep(Sleep24Hours)
            
         #turn fertilizer pump on day 3, 7,
        if current_day == 3 or current_day == 7:
            fertCounter = fertONtime
            print ""
            print "Day " + str(current_day)
            print "Fert for " +  str(fertONtime) + " Minutes"
            print "........................"
            print "Valve open, wait 10 sec"
            GPIO.output(24, 0)
            time.sleep(on10sec)
            print "Pump on"
            GPIO.output(17, 0)
            while (fertCounter > 0):
                print (str(fertCounter) + " min left")
                time.sleep(on1Min)
                fertCounter = fertCounter - 1
            GPIO.output(24, 1)
            GPIO.output(17, 1)
            print ""
            print "Completed"
            print ""
            print "--------------------------"
            time.sleep(Sleep24Hours)


        #watering on day 5,9
        if  current_day == 5 or current_day == 9:
            waterCounter = waterONtime
            print ""
            print "Day" + " " + str(current_day)
            print "Watering for " +  str(waterONtime) + " Minutes"
            print "........................"
            print "Valve open"
            GPIO.output(23, 0)
            while (waterCounter > 0):
                print (str(waterCounter) + " min left")
                time.sleep(on1Min)
                waterCounter = waterCounter - 1
            GPIO.output(23, 1)
            print ""
            print "Completed"
            print ""
            print "--------------------------"
            time.sleep(Sleep24Hours)
        
        current_day += 1        

    
  
except KeyboardInterrupt:
    print (" Quit")
    GPIO.cleanup()
  
  # Reset GPIO settings  

