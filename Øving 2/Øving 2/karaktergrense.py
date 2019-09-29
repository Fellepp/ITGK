sann = True;
while(sann):
    try:
        poengsum = int(input("Skriv inn din poengsum: "))
        if(poengsum < 0 or poengsum > 100):
            print("Ikke akseptabel input. Poengsummen må være mellom 0-100")
            continue
    except ValueError:
        print("Ikke akseptabel input. Skriv inn heltall")
        continue
    else:
        if poengsum >= 89:
            print("Du fikk A")
        elif poengsum >= 77 and poengsum <= 88:
            print("Du fikk B")
        elif poengsum >= 65 and poengsum <= 76:
            print("Du fikk C")
        elif poengsum >= 53 and poengsum <= 64:
            print("Du fikk D")
        elif poengsum >= 41 and poengsum <= 52:
            print("Du fikk E");
        else:
            print("Du fikk F")
        svar = input("Fortsette? (y/n) ")
        if svar == "n":
            sann = False;
