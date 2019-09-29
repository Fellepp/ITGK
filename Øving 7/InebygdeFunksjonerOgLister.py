import random
from collections import Counter
#a)
random_numbers = []
for i in range(0, 100):
    random_numbers.append(random.randint(0, 10))
print(random_numbers)

#b)
print(random_numbers.count(2))

#c)
print(sum(random_numbers))

#d)
random_numbers.sort()
print(random_numbers)

#e)
data = Counter(random_numbers)
print(data.most_common(1))

#f)
random_numbers.sort(reverse=True)
print(random_numbers)