#a)
def payment(billettPris, antallBilletter):
    if antallBilletter > 3:
        billettPris = billettPris - 10/billettPris*100
    return billettPris * antallBilletter

print(payment((100), 4))

#b)
def get_price(konsertnavn):
    with open("prices.txt", "r") as f:
        for line in f:
            line = line.strip()
            line = line.split(";")
            if line[0] == konsertnavn:
                return line[1]
    return -1

print(get_price("The aller beste"))

#c)
def ticket(navn, konsertnavn, antallBilletter):
    print("*****************************************")
    print("Uka 2015")
    print("*****************************************")
    totalPris = payment(int(get_price(konsertnavn)), antallBilletter)
    print("Navn:".rjust(17), navn.rjust(22))
    print("Konsert:".rjust(17), konsertnavn.rjust(22))
    print("Antall billetter:".rjust(17), str(antallBilletter).rjust(22))
    print("Totalpris:".rjust(17), str(totalPris).rjust(22))

ticket("Filip Johansen", "The aller beste", 5)

#d)
def write_to_file(navn, konsertnavn, antallBilletter, filnavn):
    totalpris = payment(int(get_price(konsertnavn)), antallBilletter)
    with open(filnavn, "a+") as f:
        f.write(konsertnavn + ";" + str(antallBilletter) + ";" + str(totalpris) + ";" + navn)
        f.write("\n")

#write_to_file("Filip Johansen", "The aller beste", 5, "concerts.txt")
#write_to_file("Siri Johansen", "Gloshaugkameratene", 2, "concerts.txt")
#write_to_file("Aleksander Olsen", "The Rectorats", 4, "concerts.txt")

#e)
def bilettInformasjon():
    info = {}
    info["The aller beste"] = ""
    info["Gloshaugkameratene"] = ""
    info["The Rectorats"] = ""
    with open("concerts.txt", "r") as f:
        for line in f:
            line = line.strip()
            line = line.split(";")
            info[line[0]] = [int(line[1]), float(line[2])]
    sum = 0
    for i in range(0, len(info)):
        sum += float(info[i][2])
        print("Konsert:".rjust(23), info[i][0].ljust(30))
        print("Antall Billetter solgt:".rjust(23), str(info[i][1]).ljust(30))
        print("Beløp innbrakt:".rjust(23), str(info[i][2]).ljust(30))
        print()
    print("Totalt samlet inn: ".rjust(23), str(sum).ljust(30))

bilettInformasjon()

