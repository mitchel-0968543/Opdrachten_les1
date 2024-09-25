import random

def dobbelspel(aantal_dobbelstenen):
    getal_min = 1
    getal_max = 6

    if aantal_dobbelstenen == 1:
        dobbelsteen1 = random.randint(getal_min, getal_max)
        print(f"Je hebt 1 dobbelsteen gegooid en jouw nummer is: {dobbelsteen1}")
    elif aantal_dobbelstenen == 2:
        dobbelsteen1 = random.randint(getal_min, getal_max)
        dobbelsteen2 = random.randint(getal_min, getal_max)
        totaalwaarde = dobbelsteen1 + dobbelsteen2
        print(f"Je hebt 2 dobbelstenen gegooid en jouw nummers zijn: {dobbelsteen1} en {dobbelsteen2}. Totaal: {totaalwaarde}")

while True:
    gameinput = input('Gooi 1 of 2 dobbelstenen (of type "stop" om te stoppen): ')
    
    if gameinput == ("stop"):
        print("Bedankt voor het spelen!")
        break
    elif gameinput == "1" or gameinput == "2":
        dobbelspel(int(gameinput))
    else:
        print('Voer alstublieft 1 of 2 in om dobbelstenen te gooien, of type "stop" om te stoppen.')
