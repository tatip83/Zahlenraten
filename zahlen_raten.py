import random

zielzahl = random.randint(1, 100)
versuche = 0

print("Willkommen zum Zahlenraten-Spiel!")
print("Ich habe eine Zahl zwischen 1 und 100 ausgewählt. Kannst du sie erraten?")

while True:
    tipp = int(input("Dein Tipp: "))
    versuche += 1

    if tipp < zielzahl:
        print("Zu niedrig! Versuch es nochmal.")
    elif tipp > zielzahl:
        print("Zu hoch! Versuch es nochmal.")
    else:
        print(f"Herzlichen Glückwunsch! Du hast die Zahl {zielzahl} in {versuche} Versuchen erraten!")
        break
    




