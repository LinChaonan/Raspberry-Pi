import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)
GPIO.setup(3,GPIO.OUT)
 
GPIO.output(3,GPIO.LOW)
for i in range(0,20):
    if GPIO.input(4)==1:
        GPIO.output(3,GPIO.HIGH)
    else:
        GPIO.output(3,GPIO.LOW)
 
    time.sleep(1)
    
    print GPIO.input(4)
