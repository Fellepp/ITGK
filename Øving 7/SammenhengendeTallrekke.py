import random

#a)
def randList(size, lower_bound, upper_bound):
    lst = []
    for i in range(0, size):
        lst.append(random.randint(lower_bound, upper_bound))
    return lst

#b)
def compareLists(list1, list2):
    equals = []
    for i in list1:
        if i in list2 and i not in equals:
            equals.append(i)
    return equals

#c)
def multiCompList(lists):
    equals = []
    for i in lists[0]:
        inAll = True
        for j in lists:
            if i not in j and i not in equals and j not in equals:
                inAll = False
        if(inAll):
            equals.append(i)
    return list(set(equals))

#d)
def longestEven(lst):
    rangeCheck = 0
    index = 0
    for i in range(0, len(lst)):
        evens = 0
        if lst[i] % 2 == 0 and lst[i] != 0:
            evens += 1
            for j in range(i+1, len(lst)):
                if lst[j] % 2 == 0:
                    evens += 1
                else:
                    break
            if evens > rangeCheck:
                rangeCheck = evens
                index = i
    return index, rangeCheck

def main():
    print(randList(10,2,7))
    a = [1,2,3]
    b = [4,3,1]
    print(compareLists(a,b))
    c = [7,2,1]
    d = [a,b,c]
    print(multiCompList(d))
    list = [4,3,3,6,2,6,8,3,4,3,3]
    print(longestEven(list))

main()