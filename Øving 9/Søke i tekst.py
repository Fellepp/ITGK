#a)
def read_from_file(filename):
    f = open(filename, "r")
    innhold = f.read()
    f.close()
    return innhold

#b)
def remove_symbols(text):
    return "".join(i for i in text if i.isalpha() or i == " ").lower()

#c)
def count_words(filename):
    dct = {}
    f = read_from_file(filename)
    ord = remove_symbols(f)
    liste = ord.split()
    for i in liste:
        if i not in dct.keys():
            dct[i] = 1
        else:
            dct[i] += 1
    return dct

#d)
print(remove_symbols("Dette er en ,SADASDASDasd, asikmf asf, ,13r0 0121+2"))
bibleDict = count_words("BIBLE.txt")
for word, value in bibleDict.items():
    print(word, value)