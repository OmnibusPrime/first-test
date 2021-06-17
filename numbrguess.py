from random import randint
zufz = randint(1, 100)
eingabe = input ('Ihre Zahl bitte: ')
eingabe = int(eingabe)
if eingabe == zufz :
        print ('Correct')
if (zufz) > eingabe:
    print ('zu niedrig')
if (zufz) < eingabe:
    print ('zu hoch')
while eingabe != zufz :
    eingabe = input ('noch eine Zahl bitte: ')
    eingabe = int(eingabe)
    if eingabe == zufz :
        print ('Correct, Congratulation!')
    if (zufz) > eingabe:
        print ('zu niedrig')
    if (zufz) < eingabe:
        print ('zu hoch')
        
# by Benjamin Graw for Univention
