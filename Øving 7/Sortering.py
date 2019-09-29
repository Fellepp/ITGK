#a)
def bubble_sort(lst):
    n = 0
    while n < len(lst):
        for i in range(0, len(lst)-n-1):
            if i < len(lst)-n:
                if lst[i] > lst[i+1]:
                    saved = lst[i]
                    lst[i] = lst[i+1]
                    lst[i+1] = saved
        n += 1
    return lst

print(bubble_sort([6,8,8,8,8,9,9,0]))

#b)
def selection_sort(lst):
    lengde = len(lst)
    nyListe = []
    while lengde > 0:
        størsteTall, størstePlass = greatestValue(lst)
        nyListe.append(størsteTall)
        lst.pop(størstePlass)
        lengde -= 1
    return nyListe

def greatestValue(lst):
    størsteTall = 0
    størstePlass = 0
    for i in range(0, len(lst)):
        if størsteTall <= lst[i]:
            størsteTall = lst[i]
            størstePlass = i
    return størsteTall, størstePlass

print(selection_sort([1,2,3,5,4,1,5,1,25,1,62]))

#c) B er raskest