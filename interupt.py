from time import sleep
import RPi.GPIO as GPIO



GPIO.setmode(GPIO.BCM)
button=17
led=4

GPIO.setup(button,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(led,GPIO.OUT)

BS=False     ##Button Status

while(1):
    if GPIO.input(button)==0:      
 ## Will continuosly read the button input. 
        print("Button was pressed")
        if BS==False:
            GPIO.output(led,True)
            BS=True
            sleep(.5)
        else:
            GPIO.output(led,False)
            BS=False
            sleep(.5)

 

### This code is completely working as a switch:
# Whenever the button is pressed the led gets high and it remain high.
# and as soon as the button is pressed again the led gets off.