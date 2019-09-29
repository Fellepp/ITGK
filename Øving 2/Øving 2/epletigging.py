sann = True
while(sann):
    print("Dette er et program for å teste din sjenerøsitet.")
    try:
        har_epler = int(input("Hvor mange epler har du? "))
        if har_epler<0:
            print("Skriv inn et positivt heltall")
            continue
    except ValueError:
        print("Skriv inn et heltall")
        continue
    else:
        if har_epler == 0:
           print("Æsj, det sier du bare for å slippe å gi noe!")
        else:
            try:
                gir_epler = int(input("Hvor mange kan du gi til meg? "))
                if gir_epler<0:
                    print("Skriv inn et positivt heltall")
                    continue
            except ValueError:
                print("Skriv inn et heltall")
                continue
            else:
                if gir_epler < har_epler / 2:
                   print("Du beholder det meste for deg selv...")
                else:
                    print("Takk, det var snilt!")
                    antall = har_epler-gir_epler
                    if antall == 1:
                        print("Du har nå 1 eple igjen.")
                    elif antall<0:
                        print("Du har nå 0 epler igjen. Gi meg de", -antall, "du skylder meg neste gang vi møtes.")
                    else:
                        print("Du har nå", antall, "epler igjen.")
    svar = input("Fortsette? (y/n) ")
    if svar == "n":
        sann = False
