#Aufgabe 1:
# Schreibe Sie ein Python-Programm, das
# 1) den Benutzter begrüßt
# 2) eine erste Zahl entgegen nimmt
# 3) eine zweite Zahl entgegen nimmt
# 4) die Summer der beiden Zahlen berechnet und ausgibt
# 5) die Diffrenz der beiden Zahlen berechnet und ausgibt
#Zusatz Differenz der kleinen von der größeren berechnen
# 6) das Produkt der beiden Zahlen berechnet und ausgibt
# 7) den Qutotient der beiden Zahlen berechnet und ausgibt (inkl. Nachkommastelle)
# Zusatz den Quotient kleinere Zahl durch die größere Zahl (inkl. Kommastellen)


print("Hallo PTO-Student")
str_Zahl1 = int(input("Eingabe EINER Zahl:")) # WICHTIG! *int*, weil sonst gehen die Mathe-Operatoren nicht weil der Text eine String-Datei ist
str_Zahl2 = int(input("Eingabe EINER weiteren Zahl:")) #float ist für Dezimalzahlen
Zahl1 = float(str_Zahl1)
Zahl2 = float(str_Zahl2)


if Zahl1 < Zahl2:
    a = Zahl1
    b = Zahl2
elif Zahl2 < Zahl1:
    a = Zahl2
    b = Zahl1
else:
    a = Zahl1
    b = Zahl2
print("Summe:",Zahl1 + Zahl2) # Summe der Zahlen
print("Differenz:" ,a - b) # Differenz der Zahlen
print("Produkt:" ,Zahl1 * Zahl2) # Produkt der Zahlen
print("Quotient:" ,a / b) # Quotient der Zahlen




