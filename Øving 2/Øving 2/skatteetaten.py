#a)
print("INFO")
print("Dette programmet besvarer om din utleie av egen bolig er skattepliktig.")
print("Først trenger vi å vite hvor stor del av boligen du har leid ut.")
print("Angi dette i prosent, 100 betyr hele boligen, 50 betyr halve,")
print("20 en mindre del av boligen som f.eks. en hybel.")

print("DATAINNHENTING: ")
betingelser = True
størrelse = int(input("Oppgi hvor mye av boligen som ble utleid: "))
if størrelse > 50:
    leieinntekt = int(input("Skriv inn hva du har hatt i leieinntekt: "))
    if leieinntekt > 20000:
        print("SKATTEBEREGNING:")
        print("Beløpet er skattepliktig")
        print("Skattepliktig beløp er", leieinntekt)
        betingelser = False
if betingelser:
    print("SKATTEBEREGNING")
    print("Skattefritt")

#b)
print("INFO")
print("Dette programmet besvarer om din utleie en annen type bolig,")
print("her sekundær- eller fritidsbolig, er skattepliktig.")
print("Først trenger vi å vite om du leier ut en sekundær- eller en fritidsbolig.")

print("DATAINNHENTING: ")
boligType = input("Skriv inn type annen bolig (sekundærbolig/fritidsbolig) du har leid ut: ")

print("INFO")
print("Du har valgt " + boligType)
if boligType == "sekundærbolig":
    print("Sekundærboliger beskattes fra første krone")
    print("Nå trenger vi først å vite hvor mange sekundærboliger du leier ut")
    print("Deretter trenger vi å vite hvor store utleieinntekter du har pr. sekundærbolig")
    print("DATAINNHENTING: ")
    antall = int(input("Hvor mange sekundærboliger leier du ut? "))
    pris = int(input("Hvor store utleieinntekter har du pr. sekundærbolig? "))
    
    skattepris = antall*pris
    
    print("SKATTEBEREGNING: ")
    print("Inntekten er skattepliktig")
    print("Skattepliktig beløp er", skattepris)
elif boligType == "fritidsbolig":
    grense = 10000
    print("Nå trenger vi først å vite om fritidsboligen(e) primært brukes til utleie eller fritid")
    print("Deretter trenger vi å vite hvor mange fritidsboliger du leier ut")
    print("Til slutt trenger vi å vite hvor store utleieinntekter du har pr. fritidsbolig")
    print("DATAINNHENTING: ")
    formål = input("Skriv inn formålet med fritidsboligen(e): (fritid/utleie) ")
    antall = int(input("Skriv inn antallet fritidsboliger du leier ut: "))
    pris = int(input("Skriv inn utleieinntekten pr. fritidsbolig: "))

    if formål == "utleie":
        skattepris = antall*pris
        print("Totalt skattepliktig beløp er", skattepris)
    elif formål == "fritid" and pris > grense:
        overskytendeBeløp = pris-grense
        skatteprosent = 0.85
        skattPrBolig = skatteprosent*overskytendeBeløp
        skattepris = skatteprosent*pris
        print("SKATTEBEREGNING: ")
        print("Inntekten er skattepliktig")
        print("Overskytende beløp pr. fritidsbolig er", overskytendeBeløp)
        print("Skattepliktig inntekt pr. fritidsbolig er", skattPrBolig)
        print("Totalt skattepliktig beløp er", skattepris)
    elif formål == "fritid" and pris <= grense:
        print("Skattefritt")
    else:
        print("Vennligst skriv fritid eller utleie og prøv igjen")       
else:
    print("Vennligst velg enten sekundærbolig eller fritidsbolig og prøv igjen")
#c)
print("INFO")
print("Dette programmet regner ut skatt for utleie av egen bolig/fritidsbolig/sekundærbolig")
svar = input("Leier du ut egen bolig? (y/n)")
if svar == "y":
    print("INFO")
    print("Dette programmet besvarer om din utleie av egen bolig er skattepliktig.")
    print("Først trenger vi å vite hvor stor del av boligen du har leid ut.")
    print("Angi dette i prosent, 100 betyr hele boligen, 50 betyr halve,")
    print("20 en mindre del av boligen som f.eks. en hybel.")

    print("DATAINNHENTING: ")
    betingelser = True
    størrelse = int(input("Oppgi hvor mye av boligen som ble utleid: "))
    if størrelse > 50:
        leieinntekt = int(input("Skriv inn hva du har hatt i leieinntekt: "))
        if leieinntekt > 20000:
            print("SKATTEBEREGNING:")
            print("Beløpet er skattepliktig")
            print("Skattepliktig beløp er", leieinntekt)
            betingelser = False
    if betingelser:
        print("SKATTEBEREGNING")
        print("Skattefritt")
elif svar == "n":
    print("INFO")
    print("Dette programmet besvarer om din utleie en annen type bolig,")
    print("her sekundær- eller fritidsbolig, er skattepliktig.")
    print("Først trenger vi å vite om du leier ut en sekundær- eller en fritidsbolig.")

    print("DATAINNHENTING: ")
    boligType = input("Skriv inn type annen bolig (sekundærbolig/fritidsbolig) du har leid ut: ")

    print("INFO")
    print("Du har valgt " + boligType)
    if boligType == "sekundærbolig":
        print("Sekundærboliger beskattes fra første krone")
        print("Nå trenger vi først å vite hvor mange sekundærboliger du leier ut")
        print("Deretter trenger vi å vite hvor store utleieinntekter du har pr. sekundærbolig")
        print("DATAINNHENTING: ")
        antall = int(input("Hvor mange sekundærboliger leier du ut? "))
        pris = int(input("Hvor store utleieinntekter har du pr. sekundærbolig? "))
        
        skattepris = antall*pris
        
        print("SKATTEBEREGNING: ")
        print("Inntekten er skattepliktig")
        print("Skattepliktig beløp er", skattepris)
    elif boligType == "fritidsbolig":
        grense = 10000
        print("Nå trenger vi først å vite om fritidsboligen(e) primært brukes til utleie eller fritid")
        print("Deretter trenger vi å vite hvor mange fritidsboliger du leier ut")
        print("Til slutt trenger vi å vite hvor store utleieinntekter du har pr. fritidsbolig")
        print("DATAINNHENTING: ")
        formål = input("Skriv inn formålet med fritidsboligen(e): (fritid/utleie) ")
        antall = int(input("Skriv inn antallet fritidsboliger du leier ut: "))
        pris = int(input("Skriv inn utleieinntekten pr. fritidsbolig: "))

        if formål == "utleie":
            skattepris = antall*pris
            print("Totalt skattepliktig beløp er", skattepris)
        elif formål == "fritid" and pris > grense:
            overskytendeBeløp = pris-grense
            skatteprosent = 0.85
            skattPrBolig = skatteprosent*overskytendeBeløp
            skattepris = skatteprosent*pris
            print("SKATTEBEREGNING: ")
            print("Inntekten er skattepliktig")
            print("Overskytende beløp pr. fritidsbolig er", overskytendeBeløp)
            print("Skattepliktig inntekt pr. fritidsbolig er", skattPrBolig)
            print("Totalt skattepliktig beløp er", skattepris)
        elif formål == "fritid" and pris <= grense:
            print("Skattefritt")
        else:
            print("Vennligst skriv fritid eller utleie og prøv igjen")       
    else:
        print("Vennligst velg enten sekundærbolig eller fritidsbolig og prøv igjen")
else:
    print("Det har skjedd en feil. Vennligst velg mellom y/n")
        
