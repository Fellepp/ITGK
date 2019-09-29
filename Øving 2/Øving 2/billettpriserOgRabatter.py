#a)
sann = True
minipris = 199
fullpris = 440
while(sann):
    try:
        dager = int(input("Dager til du skal reise? "))
        if(dager < 0):
            print("Få vekk minusen")
            continue
    except ValueError:
        print("Skriv inn heltall")
        continue
    else:
        if dager >= 14:
            print("Du kan få minipris:", minipris)
        else:
            print("For sent for minipris, du må betale fullpris:", fullpris)

        svar = input("Fortsette? (y/n) ")
        if svar == "n":
            sann = False;
    
#b)
sann = True
minipris = 199
fullpris = 440
while(sann):
    try:
        dager = int(input("Dager til du skal reise? "))
        if(dager < 0):
            print("Få vekk minusen")
            continue
    except ValueError:
        print("Skriv inn heltall")
        continue
    else:
        if dager >= 14:
            print("Du kan velge å kjøpe minipris", minipris,"- kan ikke refunderes/endres")
            valg = input("Ønskes dette? (y/n) ")
            if valg == "n":
                print("Da tilbyr vi fullpris:", fullpris)
            elif valg =="y":
                print("Takk for pengene, god reise!")
            else:
                print("Vennligst velg mellom y/n")
                continue
        else:
            print("For sent for minipris, du må betale fullpris:", fullpris)

        svar = input("Fortsette? (y/n) ")
        if svar == "n":
            sann = False;
#c)
sann = True
minipris = 199
fullpris = 440
barneRabatt = 0.5
annenRabatt = 0.75
while(sann):
    try:
        dager = int(input("Dager til du skal reise? "))
        if(dager < 0):
            print("Få vekk minusen")
            continue
    except ValueError:
        print("Skriv inn heltall")
        continue
    else:
        if dager >= 14:
            print("Du kan velge å kjøpe minipris", minipris,"- kan ikke refunderes/endres")
            valg = input("Ønskes dette? (y/n) ")
            if valg == "n":
                print("Da tilbyr vi fullpris:", fullpris)
                alder = int(input("Skriv inn din alder: "))
                if alder < 16:
                    nyPris = float(fullpris)*barneRabatt
                    print("Prisen på billetten blir:", nyPris)
                else:
                    status = input("Er du senior/militær i uniform/student? (y/n) ")
                    if status == "y":
                        nyPris = float(fullpris)*annenRabatt
                        print("Prisen på billetten blir:", nyPris)
                    else:
                        print("Prisen på billetten blir:", fullpris)
                                
            elif valg =="y":
                print("Takk for pengene, god reise!")
            else:
                print("Vennligst velg mellom y/n")
                continue
        else:
            print("For sent for minipris, du må betale fullpris:", fullpris)
            alder = int(input("Skriv inn din alder: "))
            if alder < 16:
                nyPris = float(fullpris)*barneRabatt
                print("Prisen på billetten blir:", nyPris)
            else:
                status = input("Er du senior/militær i uniform/student? (y/n) ")
                if status == "y":
                    nyPris = float(fullpris)*annenRabatt
                    print("Prisen på billetten blir:", nyPris)
                else:
                    print("Prisen på billetten blir:", fullpris)
        svar = input("Fortsette? (y/n) ")
        if svar == "n":
            sann = False;

#d)
