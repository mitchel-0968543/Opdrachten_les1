games = [
    "Players Unknown Battle Ground (PUBG) 50 2018",
    "Fortnite Battle Royale 39 2017",
    "Apex Legends 50 2019",
    "League of Legends (LOL) 27 2009",
    "Counter Strike: Global Offensive 32 2014",
    "Hearthstone 29 2020",
    "Minecraft 91 2011",
    "DOTA 2 5 2015",
    "The Division 2 N/A 2019",
    "Splatoon 2",
]

#a
print(f"A 5] {games[4]}")

#b
print(f"B {len(games[7])}")

#c "Er zitten [aantal games] games in de lijst."
print(f"Er zitten {len(games)} games in de lijst")

#d
games.insert(1, "Snake")
print(games)

#e "Helaas heeft de game [naam van de game] het niet gered om in de top 10 te blijven. We nemen waardig afscheid van [naam van de game]." Splatoon moet weg
games.remove("Splatoon 2")
print(f"Helaas heeft de game {(games)[9]} het niet gered om in de top 10 te blijven. We nemen waardig afscheid van {(games)[9]}.")


#f
games[6] = "Hearthstone 29 2012"
print(games[6])