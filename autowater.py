import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setmode(GPIO.BCM)
GPIO.setup(15, GPIO.OUT)

def valve_OnOff(Pin):
    while True:
        GPIO.output(15, GPIO.HIGH)
        print("GPIO HIGH (on), valve should be off") 
        time.sleep(10) #waiting time in seconds
        GPIO.output(15, GPIO.LOW)
        print("GPIO LOW (off), valve should be on")
        time.sleep(10)

valve_OnOff(15)

GPIO.cleanup()
