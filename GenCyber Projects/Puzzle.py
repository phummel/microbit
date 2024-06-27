# Create a multistep puzzle that invloves setting multiple peripherals
# on the micro:bit in order to solve. The puzzle box will give clues
# GenCyber Camp 2021
# Paul Hummel

from microbit import *
import music

# Caesar cipher with shift of 13
# a, b, logo, b, a, pin two
cipher = "n, o, ybtb, o, n, cva gjb"   # cipher text
stage = 0           # keep track of correct values in sequence
button_time = 200   # wait time for each button press detection in sequence
mic_level = 100     # sound level for microphone clue
light_level = 150   # light level for LED clue

mario_tune = ["E7:1","E7","R","E7","R","C7","E7","R","G7","R","R","R","G6","R","R","R",
 "C7","R","R","R","G6","R","R","E6","R","R","A6","R","B6","R","A#6","A6","R",
 "G6:2","E7","G7","A7:1","R","F7","G7","R","E7","R","C7","D7","B6","R","R",
 "C7","R","R","G6","R","R","E6","R","R","A6","R","B6","R","A#6","A6","R",
 "G6:2","E7","G7","A7:1","R","F7","G7","R","E7","R","C7","D7","B6","R","R"]

#uart.init(baudrate=9600, bits=8, parity=None, stop=1)
pin2.set_touch_mode(pin2.CAPACITIVE)         # setup pin2 for touch

while (microphone.current_event() != SoundEvent.QUIET) : # wait for mic to be quiet
    pass

display.scroll(cipher, loop=True, wait=False)   # show cipher text in background

while True:
    # 1st clue when place face down
    if (accelerometer.current_gesture() == "face down") :
        display.scroll(" ")
        music.play(music.BA_DING)
        for i in range(2):
            display.scroll("Clue: Touch Pins")
            sleep(500)
        display.clear()
        sleep(2000)
        display.scroll(cipher, loop=True, wait=False) # show cipher text in background
    
    # 2nd clue put in bright light
    if (display.read_light_level() > light_level) :
        display.scroll(" ")
        music.play(music.BA_DING)
        for i in range(2):
            display.scroll("Clue: 13")
            sleep(500)
        display.clear()
        sleep(2000)
        display.scroll(cipher, loop=True, wait=False) # show cipher text in background
    
    # 3rd clue make loud noise
    if (microphone.sound_level() >= mic_level) :
        display.scroll(" ")
        music.play(music.BA_DING)
        for i in range(2):
            display.scroll("Clue: Caesar")
            sleep(500)
        display.clear()
        sleep(2000)
        display.scroll(cipher, loop=True, wait=False) # show cipher text in background
    
    #begin test for inputs in sequence 1st button A
    if (button_a.is_pressed()) :
        stage = 1
        #display.show(1)                    # debug display
        for i in range(button_time):        # check 2nd button B
            sleep(10)
            if (button_b.is_pressed()) :
                stage = 2
                break
        if (stage == 2) :
            #display.show(2)                # debug display
            for i in range(button_time):    # check for 3rd button logo
                sleep(10)
                if (pin_logo.is_touched()) :
                    stage = 3
                    break
            if (stage == 3) :
                #display.show(3)                # debug display
                for i in range(button_time):    # check for 4th button B
                    sleep(10)
                    if (button_b.is_pressed()) :
                        stage = 4
                        break
                if (stage == 4) :
                    #display.show(4)                # debug display
                    for i in range(button_time):    # check for 5th button A
                        sleep(10)
                        if (button_a.is_pressed()) :
                            stage = 5
                            break
                    if (stage == 5) :
                        #display.show(5)                # debug display
                        for i in range(button_time):    # check for 6th button 2
                            sleep(10)
                            if (pin2.is_touched()) :
                                stage = 6
                                break
                        if (stage == 6) :               # input sequence correct
                            #display.show(6)            # debug display
                            display.scroll("")
                            display.scroll("Congratulations!!!", wait=False)
                            music.play(mario_tune)
                            sleep(3500)
                            display.scroll("")
                            display.scroll(cipher, loop=True, wait=False) # show cipher again
                        else :
                            stage = 0   # failed pin2
                    else :
                        stage = 0       # failed A (2nd)
                else :
                    stage = 0           # failed B (2nd)
            else :
                stage = 0               # failed touch
        else :
            stage = 0                   # failed B (1st)
    else :
        stage = 0                       # failed A (1st)
    
    # debug output on LED display and serial terminal
    # display.show(stage)
    # display.show(cipher)
    # brightness = display.read_light_level()
    # uart.write("The brightness is " + str(brightness) + "\r\n")
    # sleep(2000)
