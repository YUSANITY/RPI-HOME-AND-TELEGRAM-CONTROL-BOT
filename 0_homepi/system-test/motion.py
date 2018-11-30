import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(20, GPIO.IN) #PIR
GPIO.setup(21, GPIO.OUT) #BUzzer

try:
    time.sleep(2) # to stabilize sensor
    while True:
        if GPIO.input(20):
            GPIO.output(21, True)
            time.sleep(1) #Buzzer turns on for 0.5 sec
            GPIO.output(21, False)
            print("Motion Detected...")
            time.sleep(5) #to avoid multiple detection
        time.sleep(0.1) #loop delay, should be less than detection delay

except:
    GPIO.cleanup()