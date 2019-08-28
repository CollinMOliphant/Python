from flask import Flask, render_template
import RPi.GPIO as GPIO
import time
from flask import make_response
from functools import wraps, update_wrapper
from datetime import datetime

from pytz import timezone

app = Flask(__name__)

app.config["CACHE_TYPE"] = "null"
cache.init_app(app)

GPIO.setmode(GPIO.BCM)
Fertilzer_pump = 17
water_value = 23
current_day = 1
days_running = 14
pinList = [23, 17, 24]

on10sec = 10
on30sec = 30
on2Min = 120
on5Min = 300
on3Min = 180
Sleep24Hours = 86400
SleepHour = 3600
Sleep6Hours= 21600
Sleep12Hours= 43200


for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)

def nocache(view):
    @wraps(view)
    def no_cache(*args, **kwargs):
        response = make_response(view(*args, **kwargs))
        response.headers['Last-Modified'] = datetime.now()
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '-1'
        return response
    
    return update_wrapper(no_cache, view)
@app.route("/")
def hello():

   templateData = {
      'title' : 'Turn Water on'
     
      }
   return render_template('main.html', **templateData)

@app.route("/turnOn/<onTime>")
def frank(onTime):
    try:
       
        #GPIO.output(23, 0)
        #time.sleep(on2Min)
        #GPIO.output(23, 1)
        #GPIO.cleanup()
        response = "Water on for " +  int(onTime * 60) + " Minn"
   

    except KeyboardInterrupt:
        print (" Quit")
        GPIO.cleanup()

    templateData = {
    'response' : response
    }

    return render_template('waterOn.html', **templateData)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
