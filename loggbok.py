system = True

loggar = []
try:
    f = open("loggar.txt", "r") #letar om loggfilen finns
    print('laddade in logg filen')
    f.close()
except:
    f = open("loggar.txt", "w") #skapar den om den inte finns
    print('skapar logg filen')
    f.close()

while system:
    print ('1. Visa alla loggar\n2.Ny logg\n3.Spara loggar till fil\n4.Avsluta')
    try:
        val = int(input("Vad vill du göra?"))
    except:
        val = 0
    if val == 1:
        print("Visar logg")
        f = open("loggar.txt", "r") #öppnar in logg loggfilen och är i läsfunktion
        print(f.read()) #skriver ut loggfilen
        f.close()
    elif val == 2:
        print("ny logg")
        logg = input() #input stannar flödet på pogrammet och tillåter användaren till att skriva det som önskas
        loggar.append(logg) #append gör så att man lägger till det i loggfilen 
    elif val == 3:
        print("Sparar logg")
        f = open("loggar.txt", "a") #Öppnar loggfilen och lägger till det man har skrivit ifrån val 2
        for x in loggar:
            f.write(x+"\n") #f.write(x+"\n") skriver ner det man skrev i val 2 men det gör det på en ny rad
        f.close()
        loggar = []
    elif val == 4:
        print("Avslutar")
        system = False # Stänger av while loopen
    else:
        print("Prova välj av följande 1,2,3,4.")