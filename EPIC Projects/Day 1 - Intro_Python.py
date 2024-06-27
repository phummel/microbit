# Program used to introduce students to python before using micro:bit
# programiz.com -> learn python -> compiler
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# EPIC 2022
# Paul Hummel

print("Hello world")
print("What is your name?")
name = input()

#will not work!!
#input() = name

print("Hello",name,"!")
print("How old are you?")

age_str = input()  # give string for age
age = int(age_str) # convert to a number

if (age <= 18):
    print("Welcome Epic Camper!")
elif (18 < age <= 24):
    print("Welcome Epic Counselor")
else:
    print("Welcome Old Timer!")

#print hello 10 times
for count in range(10): #from 0 - 9
    print(count,": hello")

print("Guess a number:")
number = int(input()) # input number
# repeat as long as number is not 10
while (number != 10):
    print("No, guess again")
    number = int(input())
print("You Guessed 10!!")





