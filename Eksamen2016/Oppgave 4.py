D = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
     6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
     11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
     15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
     18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty',
     40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy',
     80: 'eighty', 90: 'ninety'}

L = [1000000, ' million', 1000, ' thousand', 1, '']


# a)
def i2_txt(number):
    if number in range(1, 100):
        if number in range(1, 20) or number % 10 == 0:
            return D[number]
        else:
            number1 = (number // 10) * 10
            number2 = (number % 10)
            return D[number1] + "-" + D[number2]
    else:
        return ""


print(i2_txt(5))
print(i2_txt(30))
print(i2_txt(68))


# b)
def i3_txt(number):
    if number in range(1, 1000):
        if number in range(1, 100):
            return i2_txt(number)
        else:
            number1 = number // 100
            number2 = number % 100
            return i2_txt(number1) + " hundred " + i2_txt(number2)
    else:
        return ""


print(i3_txt(100))
print(i3_txt(345))
print(i3_txt(999))


# c)
def i9_txt(number):
    if number in range(1, 1000000000):
        text = ""
        if number >= 1000000:
            text += i3_txt(number // 1000000) + " million "
            number = number % 1000000
        if number >= 1000:
            text += i3_txt(number // 1000) + " thousand "
            number = number % 1000
        if number >= 1:
            text += i3_txt(number)
        return text.strip()
    else:
        return ""


print(i9_txt(12000))
print(i9_txt(276900))
print(i9_txt(67000020))

# d)
def add_words(sentence):
    number = ""
    for char in sentence:
        if char in ("1234567890"):
            number += char
        else:
            number += " "
    number = number.strip()
    number = number.split()
    numberAsText = []
    numberIndex = []
    res = sentence.split()
    for i in range(len(number)):
        numberAsText.append(i9_txt(int(number[i])))
        numberIndex.append(res.index(number[i]))

    for i in range(0, len(number)):
        res[numberIndex[i]] += " -- " + numberAsText[i] + " --"
    print(res)
    for i in range(0, len(res)):
        res[i] += " "
    res = "".join(res)
    return res


print(add_words("I owe you 1928528 horses and 129 kicks in your balls"))
