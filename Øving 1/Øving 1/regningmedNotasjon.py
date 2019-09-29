#a)
stoff = input("Si et stoff du er i besittelse av: ")
molvekt = float(input("Hva er molvekt i gram for " + stoff + "?"))
antallGram = float(input("Hvor mange gram " + stoff + " har du?"))
avoKonst = 6.022e23
regning1 = antallGram/molvekt
regning2 = '{:.1e}'.format(regning1*avoKonst, 'e')
print("Du har", regning2, "molekyler", stoff)
