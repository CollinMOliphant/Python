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
fertONtime = int(on5Min  /  60)

waterCounter = waterONtime
fertCounter = fertONtime
  
for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)
  
try:
    while current_day <= days_running: 

        #Initializes and sets start date
        if current_day == 1 or current_day == 3 or current_day == 5 or current_day == 7 :
            print ".=====================."
            print "|    water       |" 
            print ".=====================."
            print "-----------------------"
            print "Water for" + " " + str( on2Min /  60) + " Minutes"
            print "-----------------------"
            GPIO.output(24, 0)
            while (waterCounter > 0):
                print (str(waterCounter) + " min left")
                time.sleep(on1Min)
                waterCounter = waterCounter - 1
            GPIO.output(24, 1)
            print ""
            print "Completed"
            print ""
            print "--------------------------"
            time.sleep(Sleep24Hours)

  #off on day 2,4,6,8,10,12,14
        if current_day == 2 or current_day == 4 or current_day == 6:
            print ""
            print "Day" + " " + str(current_day)
            print "Turned off"
            print ""
            print "--------------------------"
            time.sleep(Sleep24Hours)
            

        
        current_day += 1        

    
  
except KeyboardInterrupt:
    print (" Quit")
    GPIO.cleanup()  
  
  # Reset GPIO settings  

