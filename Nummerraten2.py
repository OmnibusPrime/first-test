from random import randint
def zahlenraten():
    zufallszahl = randint(1,100)
    zufallszahl = int(zufallszahl)
    eingabe = input('Ihre Zahl bitte: ')
    eingabe =int(eingabe) 
    while eingabe != zufallszahl:
        print('Falsch!')
        if (eingabe) > zufallszahl:
            print ('zu Groß')
            eingabe = input('nächste Zahl bitte ')
            eingabe =int(eingabe)
        if (eingabe) < zufallszahl:
            print ('zu klein')
            eingabe = input('nächste Zahle bitte ')
            eingabe =int(eingabe)
        if (eingabe) == zufallszahl:
            print ('Correct, Glükwunsch!')
            break
zahlenraten ()

