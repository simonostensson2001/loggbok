system = True

while system:
    print ('''
    1.Visa alla loggar
    2.Ny logg
    3.Spara loggar
    4.Avsluta
    ''')
try:
    val = int(input("Vad vill du göra?"))
except:
    val = 0
if val == 1:
    print("Visar loggar")
elif val == 2:
    print("Skapar ny logg")
elif val == 3:
    print("Sparar logg")
elif val == 4:
    print("Avslutar")
else:
    print("Prova välj av följande 1,2,3,4.")