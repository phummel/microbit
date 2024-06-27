# micro:bit Flashlight
# Button A turns the flashlight on / off
# Button B changes the brightness (0-9). Brightness will start at max (9)
#   and lower with each button press. When brightness is at 0, the next 
#   press will reset the brightness to max (9)
# GenCyber Camp 2021
# Paul Hummel

from microbit import *

light_on = False                    # default light to off
brightness = 9                      # default to light at max brightness
flash_light = Image()               # create a blank image
flash_light.fill(brightness)        # fill blank image with brightness value

while True:
    if (button_a.is_pressed()) :    # wait for button press
        if (light_on) :             # set flashlight on or off
            light_on = False
        else :
            light_on = True
        sleep(200)                  # avoid button bounce
    
    if (button_b.is_pressed()) :    # change brightness
        brightness = brightness - 1               
        if (brightness < 0) :       # if below 0, set to max
            brightness = 9
        flash_light.fill(brightness)
        sleep(200)                  # avoid button bounce

    if (light_on) :
        display.show(flash_light)   # turn on flashlight
    else :
        display.clear()             # turn flashlight off
        
