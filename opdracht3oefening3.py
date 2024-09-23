patient_exposed = input('Is de patient een volwassene of een kind?').upper()
if patient_exposed == "VOLWASSENE":
    symptomen_volwassene = input('Heeft de patient TB symptomen?').upper()
    if symptomen_volwassene == "JA":
        print('Behandel patient')
    elif symptomen_volwassene =="NEE":
        print('Verwijder patient van het ziekenhuis')
    else: print ('Abort, obekende input')

if patient_exposed == "KIND":
    symptomen_kind = input('Kan je de TB test geven, ja of nee?').upper()
    if symptomen_kind == "JA":
        print('Administer TB test')
        print('Beoordeel de testuitslag en het kind zijn of haar conditie')
    elif symptomen_kind == "NEE":
        vervolgstap_kind = input('Is het kind gezond?').upper()
        if vervolgstap_kind == 'JA':
            print('Geef preventief 6 maanden Isoniazid')
            print('Breng het kind meteen naar het ziekenhuis als hij weer symptomen laat zien')
        elif vervolgstap_kind == 'Nee':
            print('Kijk naar de volledige geschiedenis, heeft het kind al eerder TB gehad')
            print('ALs het hoogstwaarschijnlijk een TB diagnose is, behandel voor TB')      
            print('Als een andere diagnose waarschijnlijk is, behandel voor die diagnose en houdt TB in de gaten')
        else: print ('Abort, obekende input')

    else: print ('Abort, obekende input')
      
else: print ('Abort, obekende input')
