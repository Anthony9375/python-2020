import random

print("Willkommen zum Zahlen raten!")
print("Gesucht ist eine Zahl zwischen 1 und 10, du hast 5 Versuche.")

versuche = 7
zufallsZahl = random.randint(1, 100)

while versuche > 0:
    versuche -= 1
    print("Deine Schätzung:")
    inpt = input()
    a = int(inpt)
    if zufallsZahl > a:
        print("Die gessuchte Zahl ist größer.")
    if zufallsZahl < a:
        print("Die gesuchte Zahl ist kleiner.")
    elif zufallsZahl == a:
        print("Du hast die gesuchte Zahl gefunden!")
        print("Du hattest noch " + str(versuche) + " Versuche übrig.")
        break
    print("Du hast noch " + str(versuche) + " Versuche übrig.")
    if versuche == 0:
        print("Du hast leider verloren! Versuche es doch einfach noch einmal!")