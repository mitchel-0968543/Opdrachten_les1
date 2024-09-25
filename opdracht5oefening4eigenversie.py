import random

def raadspel():
    getal_max = 10
    getal_min = 5
    random_getal = random.randint(getal_min, getal_max)
    gebruikerinput = ""

    while True:
        gebruikerinput = input(f"Raad het getal van {getal_min} tot {getal_max}: ")

        # Controleer of de input een geldig getal is
        try:
            gebruikerinput = int(gebruikerinput)
        except ValueError:
            print('Voer een geldig getal in!')
            continue

        if gebruikerinput == random_getal:
            print('Geraden!')
            break
        elif gebruikerinput > getal_max:
            print(f'Getal te groot! Kies een getal tussen {getal_min} en {getal_max}.')
        elif gebruikerinput < getal_min:
            print(f'Getal te klein! Kies een getal tussen {getal_min} en {getal_max}.')
        else:
            print('Helaas, niet goed geraden.')

# De hoofd-lus waarin je kunt kiezen om nogmaals te spelen of te stoppen
while True:
    raadspel()

    # Vraag of de speler opnieuw wil spelen
    opnieuw_spelen = input("Wil je opnieuw spelen? (ja/nee): ").lower()

    if opnieuw_spelen != 'ja':
        print("Bedankt voor het spelen!")
        break