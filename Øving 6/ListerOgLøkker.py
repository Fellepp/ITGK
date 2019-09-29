#a)
number_list = []
for i in range(0, 100):
    number_list.append(i)
print(number_list)

#b)
sum = 0
for i in range(0, len(number_list)):
    if number_list[i] % 3 == 0 or number_list[i] % 10 == 0:
        sum+=i
print(sum)

#c)
for i in range(0, len(number_list), 2):
    lagring = number_list[i]
    number_list[i] = number_list[i+1]
    number_list[i+1] = lagring
print(number_list)

#d)
reversed_list = number_list
for i in range(0, len(number_list)):
    reversed_list[i] = number_list[99-i]
print(reversed_list)