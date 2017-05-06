import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(19,GPIO.OUT)
PIR_PIN = 26
GPIO.setup(PIR_PIN, GPIO.IN)

def MOTION(PIR_PIN):
	print "Motion Detection!"
	GPIO.output(19, GPIO.HIGH)
	time.sleep(2)
	GPIO.output(19, GPIO.LOW)

print "PIR test Ctrl + C"
time.sleep(2)
print "ready"

try:
	GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)
	while 1:
		time.sleep(1)

except KeyboardInterrupt:
	print "quit"
	GPIO.cleanup()

