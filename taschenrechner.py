import math

def calculator():
    while True:
        print("Willkommen beim Taschenrechner!")
        print("Wählen Sie eine der folgenden Optionen:")
        print("1. Addition")
        print("2. Subtraktion")
        print("3. Multiplikation")
        print("4. Division")
        print("5. Exponent")
        print("6. Wurzel")
        print("7. Beenden")

        choice = input("Eingabe: ")

        if choice == "1":
            num1 = float(input("Erste Zahl: "))
            num2 = float(input("Zweite Zahl: "))
            result = num1 + num2
            print("Ergebnis: ", result)
        elif choice == "2":
            num1 = float(input("Erste Zahl: "))
            num2 = float(input("Zweite Zahl: "))
            result = num1 - num2
            print("Ergebnis: ", result)
        elif choice == "3":
            num1 = float(input("Erste Zahl: "))
            num2 = float(input("Zweite Zahl: "))
            result = num1 * num2
            print("Ergebnis: ", result)
        elif choice == "4":
            num1 = float(input("Erste Zahl: "))
            num2 = float(input("Zweite Zahl: "))
            if num2 == 0:
                print("Ungültige Eingabe")
            else:
                result = num1 / num2
                print("Ergebnis: ", result)
        elif choice == "5":
            num1 = float(input("Basis: "))
            num2 = float(input("Exponent: "))
            result = num1 ** num2
            print("Ergebnis: ", result)
        elif choice == "6":
            num1 = float(input("Zahl: "))
            if num1 < 0:
                print("Ungültige Eingabe")
            else:
                result = math.sqrt(num1)
                print("Ergebnis: ", result)
        elif choice == "7":
            break
        else:
            print("Ungültige Eingabe. Bitte versuchen Sie es erneut.")

calculator()
