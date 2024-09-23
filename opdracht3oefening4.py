ordermethode = input('Wil je de order online of offline plaatsen?').upper()
if ordermethode == 'ONLINE':
    print('Uw order wordt aangemaakt')
    admin = input('Bent u een admin user?').upper()
    if admin == 'JA':
        print('Uw order is aangemaakt')
    elif admin == 'NEE':
        algemene_voorwaarden = input('Gaat u akkoord met de algemene voorwaarden, ja of nee?').upper()
        if algemene_voorwaarden == 'JA':
            print('UW order is aangemaakt')
        elif algemene_voorwaarden == 'NEE':
            print('Uw order is helaas niet goedgekeurd')
        else: print('Onbekende invoer, probeer opnieuw')
    
    else: print('Onbekende invoer, probeer opnieuw')

elif ordermethode == 'OFFLINE':
    admin = input('Bent u een admin user?').upper()
    if admin == 'JA':
        print('Uw order is aangemaakt')
    elif admin == 'NEE':
        algemene_voorwaarden = input('Gaat u akkoord met de algemene voorwaarden, ja of nee?').upper()
        if algemene_voorwaarden == 'JA':
            print('UW order is aangemaakt')
        elif algemene_voorwaarden == 'NEE':
            print('Uw order is helaas niet goedgekeurd')
        else: print('Onbekende invoer, probeer opnieuw')
        
    else: print('Onbekende invoer, probeer opnieuw')

else: print('Onbekende invoer, probeer opnieuw')
