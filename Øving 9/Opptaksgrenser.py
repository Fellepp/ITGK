#a)
def alleKomInn():
    f = open("poenggrenser_2011.csv")
    ant = 0
    for line in f:
        tekst = line.split(",")
        if tekst[1].strip() == '"Alle"':
            ant += 1
    f.close()
    return ant

#b)
def gjennomsnittNTNU():
    f = open("poenggrenser_2011.csv")
    ant = 0
    sum = 0
    for line in f:
        tekst = line.split(",")
        if line[1:5] == "NTNU":
            if tekst[1].strip() != '"Alle"':
                sum += float(tekst[1])
                ant += 1
    gjennomsnitt = round(sum/ant, 3)
    f.close()
    return gjennomsnitt

#c)
def lavest():
    f = open("poenggrenser_2011.csv")
    hittilLavest = 100
    shittyStudie = ""
    for line in f:
        tekst = line.split(",")
        if tekst[1].strip() != '"Alle"' and float(tekst[1].strip()) < hittilLavest:
            hittilLavest = float(tekst[1])
            shittyStudie = tekst[0]
    f.close()
    return shittyStudie, hittilLavest

print("Aantall studier hvor alle kom inn:", alleKomInn())
print("Gjennomsnittlig opptaksgrense for NTNU var:", gjennomsnittNTNU())
dårligst, lavest = lavest()
print("Studiet som hadde den laveste opptaksgrensen var:", dårligst + ", der var snittet:", lavest)




