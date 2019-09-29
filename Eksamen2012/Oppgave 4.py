import random


# a)
def cold_days(templist):
    days = 0
    for i in templist:
        if i < 0:
            days += 1
    return days


temps = [1, -5, 3, 0, -6, -3, 15, 0]
print(cold_days(temps))


# b)
def cap_data(array, min_value, max_value):
    result = []
    for i in array:
        if i < min_value:
            i = min_value
        elif i > max_value:
            i = max_value
        result.append(i)
    return result


A = [-70, 30, 0, 90, 23, -12, 95, 12]
result = cap_data(A, -50, 50)
print(result)


# c)
def generate_testdata(n, min_value, max_value):
    if n > abs(max_value - min_value) + 1:
        return "Feil i parametere"
    result = []
    for i in range(0, n):
        while (len(result) != i + 1):
            newNumber = random.randint(min_value, max_value)
            if newNumber not in result:
                result.append(newNumber)
    return result


print(generate_testdata(16, -5, 10))


# d)
def create_db(temp, rain, humidity, wind):
    dict = {}
    for i in range(0, len(temp)):
        dict[i + 1] = [temp[i], rain[i], humidity[i], wind[i]]
    return dict


temp = [1, 5, 3]
rain = [0, 30, 120]
humidity = [30, 50, 65]
wind = [3, 5, 7]
weather = create_db(temp, rain, humidity, wind)
print(weather)


# e)
def print_db(weather):
    print("Day".rjust(4) + "|" + "Temp".rjust(6) + "|" + "Rain".rjust(6) + "|" + "Humidity".rjust(
        10) + "|" + "Wind".rjust(6))
    print("====+======+======+==========+======")
    for i in range(0, len(weather)):
        print(str(i + 1).rjust(4), str(weather[i + 1][0]).rjust(6), str(weather[i + 1][1]).rjust(6),
              str(weather[i + 1][2]).rjust(10), str(weather[i + 1][3]).rjust(6))


print_db(weather)


# f)
def strange_weather(temp, rain):
    start = 0
    stop = 0
    leadCounter = 0
    for i in range(0, len(temp)):
        counter = 0
        if temp[i] < 0:
            counter += 1
            for j in range(i+1, len(temp)):
                if temp[j] < 0 and temp[j] < temp[j-1] and rain[j] > rain[j-1]:
                    counter += 1
                else:
                    j = j-1
                    break
            if counter > leadCounter:
                leadCounter = counter
                start = i+1
                stop = j+1
            if start == stop:
                start = 0
                stop = 0
    return start, stop


temp = [1, 3, 4, -5, -6, -7, -8, -9, 3, 0]
rain = [0, 20, 30, 0, 10, 30, 40, 0, 5, 2]
print(strange_weather(temp, rain))
