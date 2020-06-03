import RPi.GPIO as GPIO
import sys
import Adafruit_DHT
import time
try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(23,GPIO.OUT)#GPIO23
    GPIO.setup(24,GPIO.OUT)#GPIO24
    flag=0
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(11, 4)#DHT11, GPIO 4
        print (temperature)
        if(temperature>30):
            GPIO.output(23,GPIO.HIGH)
            flag=1
        if(temperature<25):
            GPIO.output(24,GPIO.HIGH)
            flag=1
        if(flag==1):
            if((temperature>25) and (temperature<33)):
                GPIO.output(23,GPIO.LOW)
                GPIO.output(24,GPIO.LOW)
                flag=0
        time.sleep(10)#for ever 10 seconds
except KeyboardInterrupt:
    GPIO.cleanup()
