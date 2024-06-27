# Program that plays a different tone/jingle based on the pin
# that is touched
# EPIC 2022
# Paul Hummel

from microbit import *
import music

#pin0.set_touch_mode(pin0.CAPACITIVE)
pin1.set_touch_mode(pin1.CAPACITIVE)
pin2.set_touch_mode(pin2.CAPACITIVE)
pin_logo.set_touch_mode(pin_logo.CAPACITIVE)

# Code in a 'while True:' loop repeats forever
while True:
#    if (pin0.is_touched()):
#        music.play(music.BIRTHDAY, wait=False)
#        display.show(0)
#        sleep(1000)
    if (pin1.is_touched()):
        #music.play(music.BLUES, wait=False)
        music.pitch(500)
        display.show(1)
        sleep(1000)
    elif (pin2.is_touched()):
        #music.play(music.CHASE, wait=False)
        music.pitch(5000)
        display.show(2)
        sleep(1000)
    elif (pin_logo.is_touched()):
        #music.play(music.DADADADUM, wait=False)
        music.pitch(10000)
        display.show("L")
        sleep(1000)
    elif (button_a.is_pressed()): #whistle
        for freq in range(100,5000,200):
            music.pitch(freq)
            sleep(50)
    else:
        music.stop()
        display.clear()
    sleep(100)



