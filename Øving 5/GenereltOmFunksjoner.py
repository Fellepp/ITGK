#a)
def multiplikasjon(x, y):
    sum = x*y
    return sum

tall1 = float(input("Tall 1: "))
tall2 = float(input("Tall 2: "))
svar = multiplikasjon(tall1, tall2)
print(svar)

#b)
def skjermSkriving(skrivTilSkjerm):
    print(skrivTilSkjerm)

tekst = input("Skriv inn tekst: ")
skjermSkriving(tekst)

#c)
def return2():
    return 2
print(return2())