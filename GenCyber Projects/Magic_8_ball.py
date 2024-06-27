# Create a magic 8 ball with the micro:bit
# GenCyber Camp 2021
# Paul Hummel

from microbit import *
import random

answers = ["Yes", "No", "Maybe", "Outlook hazy", 
            "Looks good", "Doesn't look good",
            "Ask again later", "My sources say no",
            "Outlook not so good", "It is decidedly so"]

while True:
    if (pin_logo.is_touched()) :
        guess = random.randrange(0, len(answers))
        display.scroll(answers[guess])
        sleep(200)
    #sleep(100)
