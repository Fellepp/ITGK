#a)
def number_of_lines(filename):
    f = open(filename, "r")
    antLinjer = 0
    for line in f:
        antLinjer += 1
    f.close()
    return antLinjer

#b)
def number_frequency(filename):
    f = open(filename, "r")
    tall = {}
    verdi = f.read()
    liste = verdi.split("\n")
    liste.sort()
    for i in liste:
        if i not in tall.keys():
            tall[i] = 1
        else:
            tall[i] += 1
    return tall

#c)
def dictPrinter(dict):
    for key, value in dict.items():
        for i in key:
            print(i, ": ", value)

print(number_of_lines("numbers.txt"))
print(number_frequency("numbers.txt"))
dictPrinter(number_frequency("numbers.txt"))