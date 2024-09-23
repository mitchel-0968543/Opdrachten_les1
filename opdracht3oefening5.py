hier_opeten = False
abort = False

print('Welkom bij McDonalds')
#meenemen of opeten keuze
hier_opeten = input('Wilt u hier eten of meenemen? [opeten/meenemen?]').upper()
if hier_opeten == 'OPETEN':
    hier_opeten = True
elif hier_opeten == 'MEENEMEN':
    hier_opeten = False
else: abort = True

eten_drinken = input('Burgers of drankjes?').upper()

#eetkeuze
if eten_drinken == 'BURGERS':
    burgerkeuze = input('Welke burger wil je?: Hamburger, Cheeseburger, Big Mac, Quarter Pounder').upper()
    if burgerkeuze == 'HAMBURGER':
        print('Hambuger')
    elif burgerkeuze == 'CHEESEBURGER':
        print('Cheeseburger')
    elif burgerkeuze == 'BIG MAC':
        print('Big Mac')
    elif burgerkeuze == 'QUARTER POUNDER':
        met_zonderkaas = input('Met of zonder kaas? [met/zonder]').upper()
        #quarter pounder keuze
        if met_zonderkaas == 'MET':
            print ('Quarter Pounder met kaas')
        elif met_zonderkaas == 'ZONDER':
            print ('Quarter Poudner zonder kaas')
        else: abort = True

    else: abort = True

#drankkeuze
elif eten_drinken == 'DRANKJES':
    drankkeuze = input('Wil je warme of koude dranken? [warm/koud]').upper()
    #drankkeuze warm
    if drankkeuze == 'WARM':
        drankkeuze_warm = input ('Koffie, Cappuccino of Chocolademelk?').upper()
        if drankkeuze_warm == 'KOFFIE':
            print ('Koffie')
        elif drankkeuze_warm == 'CAPPUCCINO':
            print ('Cappucino')
        elif drankkeuze_warm == 'CHOCOLADEMELK':
            print ('Chocolademelk')
        else: abort = True
    #drankkeuze koud    
    elif drankkeuze == 'KOUD':
        drankkeuze_koud = input ('Coca Cola, Cola Zero, 7-up, Fanta of Fristi?').upper()
        if drankkeuze_koud == 'COCA COLA':
            print('Coca Cola')
        elif drankkeuze_koud == 'COLA ZERO':
            print('Cola Zero')
        elif drankkeuze_koud == '7-UP':
            print('7-Up')
        elif drankkeuze_koud == 'FANTA':
            print('Fanta')
        elif drankkeuze_koud == 'FRISTI':
            print('Fristi')
        else: abort = True

    else: abort = True

else: abort = True

if abort:
    print('Onbekende invoer')
else:
    if hier_opeten:
        print ('Bedankt voor uw bestelling en eet smakelijk in ons restaurant.')
    else:
        print ('Bedankt voor uw bestelling, goede reis en eet smakelijk.')