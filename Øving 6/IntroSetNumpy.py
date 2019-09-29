#a
def allUnique(lst):
    if len(lst) == len(set(lst)):
        return True
    return False

#b
def removeDuplicates(lst):
    lst = list(set(lst))
    return lst

#c
def inAbutnotB(a, b):
    return list(set(a) - set(b))

lst = [1, 2, 3, 3, 5]
lst2 = [1, 5, 10]

print(allUnique(lst))
print(removeDuplicates(lst))
print(inAbutnotB(lst, lst2))

#Ekstraoppgave
