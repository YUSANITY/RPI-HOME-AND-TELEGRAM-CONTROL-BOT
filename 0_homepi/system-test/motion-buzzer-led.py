import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(20, GPIO.IN) 
GPIO.setup(21, GPIO.OUT) 
GPIO.setup(15, GPIO.OUT) 

try:
    time.sleep(2) # to stabilize sensor
    while True:
        if GPIO.input(20):
            GPIO.output(21, True)
            time.sleep(1) 
            GPIO.output(21, False)
	    GPIO.output(15, True)
	    time.sleep(1) 
            GPIO.output(15, False)
            print("Motion Detected...")
            time.sleep(5) #to avoid multiple detection
        time.sleep(0.1) #loop delay, should be less than detection delay

except:
    GPIO.cleanup()