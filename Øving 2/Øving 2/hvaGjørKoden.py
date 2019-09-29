#a) Variabler
#b) Dersom tekst eller float blir skrevet inn, får brukeren en feilmelding
sann = True;
while(sann):
    tall_1 = 2
    try:
        tall_2 = int(input("Skriv inn et tall: "))
    except ValueError:
        print("Ikke akseptabel input. Skriv inn heltall")
        continue
    else:
        resultat = tall_2 // tall_1
        print(resultat)
        svar = input("Fortsette? (y/n) ")
        if svar == "n":
            sann = False;
        
#c)
a = 2
b = 3
if (b<a or not b%a): #if(b%a) != 0 -> True
    b = a+b
else:
    a = a*b
print("a: ",a)
print("b: ",b)

#Printer ut a = 6, b = 3.
#Dersom både a og b = 3, printer den ut a = 3, b = 6
