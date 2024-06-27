# Virtual die that rolls a random value (1-6) displayed on LED
# Die is loaded to always roll 2 specific values under certain
# circumstances
# GenCyber Camp 2021
# Paul Hummel

from microbit import *
import random
import utime
import speech

pin2.set_touch_mode(pin2.CAPACITIVE)    #turn pin2 to capacitive mode
display.show(Image.SQUARE)

while True:
    if (accelerometer.current_gesture() == "shake") :
        random.seed(utime.ticks_ms())
        for i in range(80,200,10) :
            display.show(123456,wait=False,loop=True,delay=i)
            sleep(1000-(2*i))
        roll = random.randint(1,6)
        if (pin2.is_touched()) :
            display.show(6)
            speech.say("You rolled a 6", speed=120, pitch=100, throat=100, mouth=200)
            sleep(1000)
            speech.say("Or did you", speed=120, pitch=100, throat=100, mouth=200)
        elif (pin_logo.is_touched()) :
            display.show(4)
            speech.say("You rolled a 4", speed=120, pitch=100, throat=100, mouth=200)
            sleep(1000)
            speech.say("Or did you", speed=120, pitch=100, throat=100, mouth=200)
        else :
            display.show(roll)
            line = "You rolled a " + str(roll)
            speech.say(line, speed=120, pitch=100, throat=100, mouth=200)
            
        
