import random
import time
sum = 0
pris = 5
brukt = 0
førstePlass = 0
andrePlass = 0
tredjePlass = 0
fjerdePlass = 0
femtePlass = 0
tap = 0
seier = 0
førstePremie = 2749455
andrePremie = 102110
tredjePremie = 3385
fjerdePremie = 95
femtePremie = 45

program_starts = time.time()

antallForsøk = int(input("Hvor mange ganger vil du forsøke å vinne i lotto? "))
for i in range(0,antallForsøk):
    now = time.time()
    print(i, round(i/antallForsøk*100, 2), "% fullført . . .")
    brukt += pris
    #a)
    numbers = []
    for i in range(1, 35):
        numbers.append(i)
    ##print(numbers)

    #b)
    myGuess = [1,2,3,4,5,6,7]
    """for i in range(0, 7):
        myGuess.append(int(input("Skriv inn et tall mellom 1, 34")))"""

    #c)
    def getNumbers(list, n):
        numbersPicked = []
        antallTrekk = 0
        while antallTrekk < n:
            trekk = random.randint(1, len(list))
            if trekk not in numbersPicked:
                numbersPicked.append(trekk)
                antallTrekk += 1
        return numbersPicked
    tall = getNumbers(numbers, 10)
    ##print(tall)

    #d, f)
    def compList(list1, list2):
        lottoTall = []
        tilleggsTall = []
        for i in range(0, 7):
            lottoTall.append(list1[i])
        for i in range(7, 10):
            tilleggsTall.append(list1[i])
        return len(set(lottoTall).intersection(list2)), len(set(tilleggsTall).intersection(list2))
    antallRiktige, tilleggsTall = compList(tall, myGuess)
    ##print(antallRiktige, tilleggsTall)

    #e)
    def premie(tall1, tall2):
        if tall1 > 6:
            return førstePremie
        elif tall1 == 6 and tall2 >= 1:
            return andrePremie
        elif tall1 == 6 and tall2 == 0:
            return tredjePremie
        elif tall1 == 5:
            return fjerdePremie
        elif tall1 == 4 and tall2 >= 1:
            return femtePremie
        else:
            return 0

    premie = premie(antallRiktige, tilleggsTall)
    if premie == førstePremie:
        førstePlass += 1
        sum += førstePremie
        seier += 1
    elif premie == andrePremie:
        andrePlass += 1
        sum += andrePremie
        seier += 1
    elif premie == tredjePremie:
        tredjePlass += 1
        sum += tredjePremie
        seier += 1
    elif premie == fjerdePremie:
        fjerdePlass += 1
        sum += fjerdePremie
        seier += 1
    elif premie == femtePremie:
        femtePlass += 1
        sum += femtePremie
        seier += 1
    else:
        tap += 1

totSum = sum-brukt
print("Antall forsøk:", antallForsøk,
      "\nAntall førsteplass:", førstePlass, "\nAntall andreplass:", andrePlass,
      "\nAntall tredjeplass:", tredjePlass, "\nAntall fjerdeplass:", fjerdePlass,
      "\nAntall femteplass:", femtePlass, "\nAntall tap:", tap, "\nAntall seiere:", seier,
      "\nPenger vunnet:", sum, "\nPenger brukt:", brukt, "\nSum i total:", totSum)
#g)