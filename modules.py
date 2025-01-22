from random import randint

def show_divided_numbers(num1, num2):
    results = []
    for i in range(1,1401):
        if i % num1 == 0 and i % num2 == 0:
            results.append(i)

    return results

def start_game():
    guessed_number = randint(1,40)

    choice = int(input("gissa talet mellan 1 och 40: "))
    while choice != guessed_number:
        print("Du gissade fel ")
        if choice < guessed_number:
            print("Talet är större än din gissning, försök igen ")
        elif choice > guessed_number:
            print("Talet är mindre än din gissning, försök igen")

        choice = int(input("gissa talet mellan 1 och 40: "))

    print("Du gissade rätt, bra jobbat ")

