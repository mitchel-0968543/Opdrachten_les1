
user_input = ""
while user_input != ".":
    user_input = input("Please enter a number (or say stop to stop): ")
    if user_input == "stop":
        print("Goodbye")
        break
    else:
        number_input = int(user_input)
        numbers = list(range(2, number_input - 1))
        priemgetal = True
        for deler in numbers:
            if deler < number_input:
                if number_input % deler == 0:
                    priemgetal = False
                    break
        if priemgetal:
            print("Is prime: " + str(user_input))
        else:
            print("Not prime: " + str(user_input))




