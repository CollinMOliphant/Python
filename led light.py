import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(19,GPIO.OUT)
print"on"
GPIO.output(19, GPIO.HIGH)
time.sleep(1)
print"Loff"
GPIO.output(19, GPIO.LOW)
