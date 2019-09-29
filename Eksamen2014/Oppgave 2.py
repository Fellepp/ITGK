# a)
def inputPerson():
    name = input("Name: ")
    id = input("ID: ")
    kg = int(input("Kg: "))
    size = int(input("Size: "))
    return [name, id, kg, size]


# print(inputPerson())


# b)
def readDbFile(filename):
    medlemsTabell = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            line = line.split(";")
            medlemsTabell.append([line[0], line[1], line[2], line[3]])
    return medlemsTabell


db = readDbFile("members.txt")
for line in db:
    print(line)


# c)
def printMemberList(medlemsTabell):
    print("NAVN".ljust(15), "ID-NR".rjust(9), "VEKT".rjust(5), "kg", "SKJERMSTØRRELSE".rjust(4))
    for line in medlemsTabell:
        print(line[0].ljust(15), line[1].rjust(9), str(line[2]).rjust(5), "kg", str(line[3]).rjust(4), "kvadratfot")


printMemberList(db)


# d)
def addPerson(filename):
    person = inputPerson()
    with open(filename, "a+") as f:
        f.write("\n" + person[0] + ";" + person[1] + ";" + str(person[2]) + ";" + str(person[3]))
    printMemberList(readDbFile(filename))


# addPerson("members.txt")

# e)
def feet2seconds(feet):
    v0 = 100
    v1 = 200
    skjermhøyde = 3000
    fallhøyde = feet - skjermhøyde
    if feet < skjermhøyde:
        return 0
    elif fallhøyde < 1000:
        return fallhøyde / v0
    else:
        return (1000/v0 + (fallhøyde-1000)/v1)

print(feet2seconds(10000))



