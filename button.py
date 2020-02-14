
## This code is a basic working of a push button.
## When the button is pressed LED gets on and as soon as
## button is released led get's off.

## Also the led is by default off.

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

sleepTime= .1

led=4
button=17


GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led, GPIO.OUT)  
GPIO.output(led,False)     ## LED will remain off by-default.

try:
    while True:
        GPIO.output(led, not GPIO.input(button))
        #sleep(.1)
finally:
    GPIO.output(led,False)
    GPIO.cleanup()
