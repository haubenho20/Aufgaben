# einfache '=' Zeichen: ist eine Zuweisung
strWetter = input("Wochenendwetter - 'sonnig' oder 'regnerisch' ")

# doppeltes '==' Zeichen ist ein Vergleichsoperator
if strWetter == "sonnig":
    print("Gartenparty")
elif strWetter == "regnerische": #else if
    print("Kellerparty")
else:
    print("bitte 'sonnig' oder 'regnerisch' eintragen!")
# bei Problemen:
# Debugger starten (strg F5)
# große Schritte F6
# klein Schritte F7
