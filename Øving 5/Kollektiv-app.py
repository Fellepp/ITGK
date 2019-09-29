#a)
def billettPris(alder, sykkel):
    sum = 0
    if sykkel == "j":
        sum = 50
    if alder > 60 or alder < 5:
        return sum
    elif 5<=alder<=20:
        sum += 20
        return sum
    elif 21<=alder<=25:
        sum += 50
        return sum
    elif 26<=alder<=60:
        sum += 80
        return sum

kjøper = True
totalSum = 0
while(kjøper):
    sjekkAlder = int(input("Hvor gammel er du? "))
    sykkel = input("Har du med deg sykkel (j/n)? ")
    print("Denne billetten koster", billettPris(sjekkAlder, sykkel))
    totalSum += billettPris(sjekkAlder, sykkel)
    print("Du er nå oppe i", totalSum)
    kjøpeFler = input("Skal du ha flere billetter (j/n)? ")
    if kjøpeFler == "n":
        kjøper = False

print("Du må betale", totalSum)