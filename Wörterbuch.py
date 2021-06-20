# Erweitere das Wörterbuch-Beispiel um die Möglichkeit, Einträge zu ergänzen bzw. zu löschen

woerterbuch_deutsch = ["Apfel", "Birne", "Kirsche", "Melone", "Marille", "Pfirsich"]
print(woerterbuch_deutsch)
woerterbuch_englisch = ["apple", "pear", "cherry", "melon", "apricot", "peach"]
max = len(woerterbuch_deutsch)

auswahl = input("Was möchten Sie tun? Befehl? \n [E]ingabe,  \n [L]öschen, \n [A]bfrage:")

if auswahl == 'E' or 'e' : # Einfügen
    Wort = input("Bitte geben Sie ihr deutsches Wort ein: ")
    woerterbuch_deutsch.append(Wort) # Wort (Variable) in die Liste hinzufügen
    Word = input("Bitte geben Sie Ihr englisches Wort ein: ")
    woerterbuch_englisch.append(Word)
    
    print(woerterbuch_deutsch)
    print(woerterbuch_englisch)
    

elif auswahl == 'L' or 'l' : # Löschen
    Wort = input("welches Wort möchten Sie löschen?")


else: Wort = input()#Standardvorgang  immer mit dem geringsten Risiko
    # Abfrage



index = 0

eingabe = input("Deutscher Begriff: ")
while index < max:
    if woerterbuch_deutsch[index].lower() == eingabe.lower():
        print(woerterbuch_englisch[index])
        break
    index += 1
if index == max:
    print("nicht gefunden")

# number_list = [[1,2,3],[4,5,6],[7,8,9]]
# print(number_list[0][1])

