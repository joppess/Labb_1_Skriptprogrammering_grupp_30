from random import randint # importerar randint från Random-module


def show_divided_numbers(num1, num2): # vi definierar funktionen med två parametrar
    results = [] # lista
    for i in range(1,1401): # for-loop för varje siffra mellan 1 och 1400
        if i % num1 == 0 and i % num2 == 0: # (if-sats) om valda siffran är delbar med num1 och num2 utan ge någon rest
            results.append(i) # lägg siffran "i" till listan

    return results # vi returnerar listan

def start_game(): #funktion
    guessed_number = randint(1,40) # slumpa fram ett tal mellan 1 och 40 som sparas i variabel


    choice = int(input("\ngissa talet mellan 1 och 40: ")) # vi sparar användarens val i choice genom att konvertera inputen till en int
    while choice != guessed_number: # while-loop för att loopa så länge gissningen är fel/falsk
        print("Du gissade fel ")
        if choice < guessed_number: # kolla om gissningen är mindre än det slumpade talet
            print("Talet är större än din gissning, försök igen ")
        elif choice > guessed_number: # kolla om gissningen är större än det slumpade talet
            print("Talet är mindre än din gissning, försök igen")

        # ge användaren en ny chans att gissa och börja om loopen
        choice = int(input("gissa talet mellan 1 och 40: "))

    # användaren gissade rätt, skriv ut ett meddelande som gratulerar
    print("Du gissade rätt, bra jobbat ")

