# Program that creates a chat client using the micro:bit wireless
# radio to create an ad-hoc mesh network. Uses button A when
# wanting to send a message
# EPIC 2022
# Paul Hummel

from microbit import *
import radio
import music

#for my sanity
set_volume(64)

radio.config(group=32)
radio.on()

print("Enter Username for chat:")
name = input()

# Code in a 'while True:' loop repeats forever
while True:
    message = radio.receive()
    if (message):
        print(message)
        if (message.find(":)") != -1):
            display.show(Image.HAPPY)
        if (message.find(":(") != -1):
            display.show(Image.SAD)
        if (message.find("Happy Birthday") != -1):
            music.play(music.BIRTHDAY, wait=False)
    if (button_a.is_pressed()):
        print("What do you want to send?")
        text = input()
        radio.send(name+" : "+text)
        sleep(100)
    
