import modules # vi importerar metoderna från modules.py
first = int(input("Skriv in första talet: ")) # vi frågar användaren och sparar svaret i en variabel
second = int(input("Skriv in det andra talet: "))

print(f"Resultat: {modules.show_divided_numbers(first, second)}") # vi skriver ut resultatet från metoden show_divided_numbers

modules.start_game() # vi startar spelet genom att anropa start_game

print ("Programmet avslutas ") # programmet avslutas

print("Hello")
