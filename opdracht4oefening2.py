# a] Geef in een volzin het aantal computer leveranciers in de tuple. "De tuple bevat [aantal computer leveranciers] computer leveranciers."

# b] Geef in een volzin het aantal karakters van computer leverencier nummer 8; "De naam van [Naam computer leverancier] bestaat uit [aantal karakters] karakters."

# c] Geef de naam van de computer leverancier op de 10de plaats

tuple = ("Apple", "Asus", "Dell", "Lenovo", "Acer", "Samsung", "MSI", "Hewlett-Packard (HP)", "Toshiba", "Microsoft", "Chuwi", "Sony")

# a]
print(f"De tuple bevat {len(tuple)} computer leveranciers.")

# b]
print(f"De naam van {tuple[7]} bestaat uit {len(tuple[7])} karakters.")

# c]
print(f"{tuple[9]}")