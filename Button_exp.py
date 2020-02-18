
#### EXPERIMENTAL FILE ########




from time import sleep
import RPi.GPIO as GPIO



GPIO.setmode(GPIO.BCM)
button=17
led=4

GPIO.setup(button,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(led,GPIO.OUT)

BS=False     ##Button Status
GPIO.output(led,True)


while(1):
    if GPIO.input(button)==0:      
 ## Will continuosly read the button input. 
        print("Button was pressed")
        print(button)
        GPIO.output(led,False)
        sleep(.10)
        GPIO.output(led,True)
GPIO.cleanup()
       