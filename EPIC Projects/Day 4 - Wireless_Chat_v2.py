# Program that creates a chat client using the micro:bit wireless
# radio to create an ad-hoc mesh network. Does not need to button A
# to indicate sending a message
# EPIC 2022
# Paul Hummel

from microbit import *
import radio
import music

radio.config(group=13)
radio.on()

print("What is your username?")
name = input()

# Code in a 'while True:' loop repeats forever
while True:
    message = radio.receive()
    if message:
        if (message.find(":)") != -1):
            display.show(Image.HAPPY)
        elif (message.find("<3") != -1):
            display.show(Image.HEART)
        elif (message.find("happy birthday") != -1):
            music.play(music.BIRTHDAY, wait=False)
        else:
            display.clear()
        print(message)
    if (uart.any()):
        print("What message do you want to send?")
        message_send = input()
        radio.send(name+" : "+message_send)

