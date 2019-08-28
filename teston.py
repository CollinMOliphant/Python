import RPi.GPIO as GPIO  
import time  
from datetime import datetime
from pytz import timezone

GPIO.setmode(GPIO.BCM)

fmt = "%m-%d %H:%M:%S"
now_utc = datetime.now(timezone('UTC'))
now_pacific = now_utc.astimezone(timezone('US/Pacific'))   

Fertilzer_pump = 17
water_value = 23
current_day = 1
days_running = 14
pinList = [23, 17, 24] 

on10sec = 10  
on2Min = 120
on5Min = 300
on3Min = 180
Sleep24Hours = 86400 
SleepHour = 3600
Sleep6Hours= 21600
Sleep12Hours= 43200

#1 monday | water
#2 tue
#3 wed    | fert
#4 thur
#5 friday | water
#6 sat
#7 sun    | fert

#8 monday
#9 tue    | water
#10 wed
#11 thurd | fert
#12 fri
#13 sat   | water
#14 sun
  
for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)
  
try:
    while current_day <= days_running: 

        #Initializes and sets start date
        if current_day == 1:
            print ".=====================."
            print "|    TEST PUMPS       |" 
            print ".=====================."
            print "-----------------------"
            print "Water for" + " " + str( on10sec /  60) + " Minutes"
            print "-----------------------"
            GPIO.output(23, 0)
            time.sleep(on10sec)
            GPIO.output(23, 1)
            print "-----------------------"
            print "Fert for" + " " + str( on10sec /  60) + " Minutes"
            print "valve open, wait 10 sec"
            GPIO.output(24, 0)
            time.sleep(on10sec)
            print "pump on"
            GPIO.output(17, 0)
            print "-----------------------"
            time.sleep(on10sec)
            GPIO.output(24, 1)
            GPIO.output(17, 1)

            

        
        current_day += 1        

    
  
except KeyboardInterrupt:
    print (" Quit")
    GPIO.cleanup()  
  
  # Reset GPIO settings  

