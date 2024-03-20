#!/usr/bin/python3
import random   #library
n = 20
to_be_guessed = random.randint(1,n)  #integer Zufallszahl zwischen 1 und 20

guess = 0
while guess != to_be_guessed:
    guess = int(input("Neuer Versuch: "))
    if guess > 0:
        if guess > to_be_guessed:
            print("Zu gross")
        elif guess < to_be_guessed:
            print("Zu klein")
    else:
        print("Schade, dass du aufgibst!")
        break
else:
    print("Gratuliere, das war's")

