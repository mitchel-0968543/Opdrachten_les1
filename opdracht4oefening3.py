dictionary = {
"The Simpsons": "636-555-3226",
"Vegas Vacation": "555-0100",
"Ghostbusters": "555-23678",
"Billy Madison": "555-0840",
"Swingers": "213-555-4679",
"Bruce Almighty": "555-0123",
"Seinfeld": "555-FILK",
"Arrested Development": "555-0113",
"Die Hard With a Vengeance": "555-0001",
"The A-Team": "555-6162"
} 
print(dictionary)

#a] Geef het telefoonnummer van Bruce Almigthy in de volzin: "Het telefoonnummer van Bruce Almighty is [telefoonnummer]."

#b] Voeg het telefoonnummer van de Harry Potter toe, nummer: 605-475-6961 aan de dictionary.

#c] Pas het telefoonnummer van de Ghostbusters aan. Dit moet zijn 555-2368. Geef in een volzin weer. "Het telefoonnummer [telefoonnummer] van de Ghostbusters is gewijzigd naar [nieuwe nummer]."

#d] Verwijder het telefoonnummer van Seinfeld. Gebruik de volzin: "Telefoonnummer [telefoonnummer] van Seinfeld is verwijderd."

#e] Geef aan hoeveel telefoonnummers er nu in dictionary zitten. Gebruik de volzin: "In de dictionary zitten [aantal telefoonnummers] telefoonnummers."


#A 

telefoonnummer = dictionary["Bruce Almighty"]
print(f"Het telefoonnummer van Bruce Almighty is {telefoonnummer}")

#B

dictionary["Harry Potter"] = "605-475-6961"
print(f"Het telefoonnummer van Harry Potter is {dictionary["Harry Potter"]}")

#C

oud_nummer = dictionary["Ghostbusters"]
dictionary["Ghostbusters"] = "555-23785468"
print(f"Het telefoonnummer {oud_nummer} van de Ghostbusters is gewijzigd naar {dictionary["Ghostbusters"]}.")

#D

telefoonnummer_2 = dictionary["Seinfeld"]
del dictionary["Seinfeld"]
print(f"Telefoonnummer {telefoonnummer_2} van Seinfeld is verwijderd.")

#E

aantal_telefoon = len(dictionary)
print(f"In de dictionary zitten {aantal_telefoon} telefoonnummers.")

