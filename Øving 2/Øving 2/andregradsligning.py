sann = True
while(sann):
    a = int(input("Skriv inn a (antall x^2) "))
    b = int(input("Skriv inn b (antall x) "))
    c = int(input("Skriv inn c "))

    d = b**2-4*a*c

    setning = "Andregradsligningen " + str(a) + "x^2 + " + str(b) + "x + " + str(c)

    if d<0:
        d = d-(d*2)
        r = -b/(2*a)
        i = round((d**0.5)/4, 2)
        print(setning + " har to imaginære løsninger.")
        print(str(r) + " +- " + str(i) + "i");
    elif d>0:
        x1 = (-b+(d**0.5))/(2*a)
        x2 = (-b-(d**0.5))/(2*a)
        print(setning + " har to reelle løsninger.")
        print("x1 = " + str(x1) + ", x2 = " + str(x2))
    else:
        x = (-b/(2*a))
        print(setning + " har en reell løsning.")
        print("x = " + str(x))
        
    sjekk = input("Kjøre programmet igjen? y/n ")
    if sjekk == "n":
        sann = False
