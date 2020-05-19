system = True

try:
    f = open("loggar.txt", "r")
    print('laddade in logg filen')
    f.close()
except:
    f = open("loggar.txt", "w")
    print('skapar logg filen')
    f.close()


while system:
    print ('1. Visa alla loggar\n2.Ny logg\n3.Spara loggar till fil\n4.Avsluta')
try:
    val = int(input("Vad vill du göra?"))
except:
    val = 0
if val == 1:
    print("Visar loggar")
    f = open("loggar.txt", "r")
    print(f.read()) 
    f.close()
elif val == 2:
    print("ny logg")
elif val == 3:
    print("Sparar logg")
elif val == 4:
    print("Avslutar")
    system = False 
else:
    print("Prova välj av följande 1,2,3,4.")
