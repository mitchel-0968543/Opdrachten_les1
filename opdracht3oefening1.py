connection_choice_question = input('Met welk netwerk wilt u verbonden worden: 4G, 5G of Open Wifi?').upper()

if connection_choice_question == "4G":
    print(f'U bent verbonden met 4G!')
elif connection_choice_question == "5G":
    print(f'U bent verbonden met 5G!')
elif connection_choice_question == "OPEN WIFI":
    answer_wifi = (input(f'Weet u zeker dat u met dit netwerk wil verbinden? Ja of Nee?'))
    answer = answer_wifi.upper()
    if answer == "JA":
        print(f'U bent verbonden met open Wifi')
    elif answer_wifi == "NEE":
        print(f'De verbinding is afgebroken')
else:
    print(f'Onbekende invoer, probeer opnieuw.')
