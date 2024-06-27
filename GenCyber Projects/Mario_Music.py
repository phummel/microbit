# Create program to play various tunes from the original Super Mario Brothers
# Note order derived from https://github.com/robsoncouto/arduino-songs/
# GenCyber Camp 2021
# Paul Hummel

from microbit import *
import music

mario_tune = ["E7:1","E7","R","E7","R","C7","E7","R","G7","R","R","R","G6","R","R","R",
 "C7","R","R","R","G6","R","R","E6","R","R","A6","R","B6","R","A#6","A6","R",
 "G6:2","E7","G7","A7:1","R","F7","G7","R","E7","R","C7","D7","B6","R","R",
 "C7","R","R","G6","R","R","E6","R","R","A6","R","B6","R","A#6","A6","R",
 "G6:2","E7","G7","A7:1","R","F7","G7","R","E7","R","C7","D7","B6","R","R"]

mario_underworld = [
"C4:2","C5","A3","A4",
"A#3", "A#4","R:3",
"R:4",
"C4:2","C5","A3","A4",
"A#3", "A#4","R:3",
"R:4",
"F3:2","F4","D3","D4",
"D#3","D#4","R:3",
"R:4",
"F3:2","F4","D3","D4",
"D#3","D#4","R:3",
"R","D#4:1","C#4","D4",
"C#4:3","D#4",
"D#4","G#3",
"G3","C#4",
"C4:1","F#4","F4","E3","A#4","A4",
"G#4:2","D#4","B3",
"A#3","A3","G#3",
"R:4","R","R"]

music.play(mario_tune)
music.play(mario_tune)
music.play(mario_underworld)

while True:
    display.scroll("Hello, World!")
    sleep(2000)
