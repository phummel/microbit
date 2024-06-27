# Program expands on Caesar cipher to encode and decode text
# Uses serial terminal for intput / output
# EPIC 2022
# Paul Hummel

from microbit import *

cipher_shift = 3
cipher_text = ""

# Code in a 'while True:' loop repeats forever
while True:
    print("[1] Encrypt Message")
    print("[2] Decrypt Message")
    mode = int(input())
    if (mode == 1):
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
    elif (mode == 2):
        print("Enter cipher text to decrypt:")
        message = input()
        for cipher_shift in range(26,0,-1):
            decrypt_text = ""
            for i in range(len(message)):
                letter = ord(message[i]) + cipher_shift
                if (letter > 122):
                    letter = letter - 26
                decrypt_text = decrypt_text + chr(letter)
            print(26-cipher_shift,":",decrypt_text)    
    





        
