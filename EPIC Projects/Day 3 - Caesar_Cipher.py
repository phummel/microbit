# Program used to introduce students to Caesar cipher using python
# Uses serial for input / output
# Paul Hummel

from microbit import *

cipher_shift = 3
cipher_text = ""

# Code in a 'while True:' loop repeats forever
while True:
    print("Enter message to encrypt:")
    message = input()
    print("What Caesar shift to encrypt (0-26):")
    cipher_shift = int(input())
    cipher_text = ""
    for i in range(len(message)):
        letter = ord(message[i]) + cipher_shift
        if (letter > 122):
            letter = letter - 26
        cipher_text = cipher_text + chr(letter)
        #print(message[i],":",chr(letter))
    print("Cipher:",cipher_text)    
    
    





        
