import RPi.GPIO as GPIO
import sys
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pin =  15 # pin 11 on the RP board
GPIO.setup(pin, GPIO.OUT)
state = int(sys.argv[1])
GPIO.output(pin, (GPIO.LOW if state == 0 else GPIO.HIGH))
