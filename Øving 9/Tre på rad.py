def lag_brett():
    global brett
    print("    1   2   3")
    print("  -------------")
    print("1 | " + brett[0][0] + " | " + brett[0][1] + " | " + brett[0][2] + " |")
    print("  -------------")
    print("2 | " + brett[1][0] + " | " + brett[1][1] + " | " + brett[1][2] + " |")
    print("  -------------")
    print("3 | " + brett[2][0] + " | " + brett[2][1] + " | " + brett[2][2] + " |")
    return brett


def navn():
    global navn1, navn2
    navn1 = input("Skriv inn navn på den første spilleren ")
    navn2 = input("Skriv inn navn på den andre spilleren ")


def vunnet(sisteTrekk):
    global brett
    verdi = brett[int(sisteTrekk[1]) - 1][int(sisteTrekk[0]) - 1]
    like1 = 0
    like2 = 0
    like3 = 0
    like4 = 0
    for i in range(3):
        if brett[i][int(sisteTrekk[0]) - 1] == verdi:
            like1 += 1
        if brett[int(sisteTrekk[1]) - 1][i] == verdi:
            like2 += 1
        if brett[i][i] == verdi:
            like3 += 1
        if brett[i][2 - i] == verdi:
            like4 += 1
    if like1 == 3 or like2 == 3 or like3 == 3 or like4 == 3:
        return True
    return False


def lovlig_trekk(trekk):
    global brett
    if brett[int(trekk[1]) - 1][int(trekk[0]) - 1] != " ":
        return False
    return True


def gyldig_input(trekk, tegn):
    if int(trekk[0]) < 0 or int(trekk[0]) > 2:
        return False
    if int(trekk[1]) < 0 or int(trekk[1]) > 2:
        return False
    if tegn != "x" or tegn != "o":
        return False
    return True


navn1 = ""
navn2 = ""
brett = []
for i in range(3):
    brett.append([" ", " ", " "])


def main():
    global navn1, navn2, brett
    navn()
    lag_brett()
    ferdig = False
    while not ferdig:
        trekk1 = input("Skriv inn trekk for spiller 1 ").split(",")
        while not gyldig_input(trekk1, trekk1[2]) and not lovlig_trekk(trekk1):
            trekk1 = input("Ikke gyldig input. Skriv inn trekk for spiller 1 ").split(",")
        brett[int(trekk1[1]) - 1][int(trekk1[0]) - 1] = trekk1[2]
        lag_brett()
        if not vunnet(trekk1):
            trekk2 = input("Skriv inn trekk for spiller 2 ").split(",")
            while not gyldig_input(trekk2, trekk2[2]) and not lovlig_trekk(trekk2):
                trekk2 = input("Ikke gyldig input. Skriv inn trekk for spiller 1 ").split(",")
            brett[int(trekk2[1]) - 1][int(trekk2[0]) - 1] = trekk2[2]
            lag_brett()
            if vunnet(trekk2):
                ferdig = True
                print("Spiller 2 vant")
        else:
            print("Spiller 1 vant")
            ferdig = True


main()