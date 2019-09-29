#a)
def is_six_at_edge(list):
    if list[0] == 6 or list[len(list)-1] == 6:
        return True
    else:
        return False

#b)
def average(list):
    return sum(list)/len(list)

#c)
def median(list):
    list.sort()
    return list[int(len(list)/2)]

list = [1,2,3,4,5,6,7]
print(is_six_at_edge(list))
print(average(list))
print(median(list))