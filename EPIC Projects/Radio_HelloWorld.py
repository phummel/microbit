# Program that sends a message via the wireless radio when the
# logo is touched.
# EPIC 2022
# Paul Hummel

from microbit import *
import radio

# Setup radio
radio.config(group=23)
radio.on()

# Code in a 'while True:' loop repeats forever
while True:
    if pin_logo.is_touched():
        radio.send('hello world')
        sleep(1000)
    message = radio.receive()
    if message:
        display.scroll(message)
