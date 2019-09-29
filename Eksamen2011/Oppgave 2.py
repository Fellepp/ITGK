# a)
listerep = [3, 1, 5, 4, 4, 5, 2, 4, 1, 2]


def edgeLength(x0, y0, x1, y1):
    return round(((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5, 2)


print(edgeLength(3, 1, 5, 4))


# b)
def circumference(pList):
    lengde = len(pList)
    if lengde % 2 != 0 or lengde == 0:
        return -1
    elif lengde == 2:
        return 0
    elif lengde == 4:
        return 2 * edgeLength(pList[0], pList[1], pList[2], pList[3])
    else:
        sum = 0
        for i in range(0, lengde - 2, 2):
            sum += edgeLength(pList[i], pList[i + 1], pList[i + 2], pList[i + 3])
        sum += edgeLength(pList[0], pList[1], pList[lengde - 2], pList[lengde - 1])
    return sum


print(circumference(listerep))


# c)
def enclosingRectangle(pList):
    xlow = min(pList[::2])
    xhigh = max(pList[::2])
    ylow = min(pList[1::2])
    yhigh = max(pList[1::2])
    return [xlow, ylow, xhigh, yhigh]


print(enclosingRectangle(listerep))

#d)
def readPolygonFile(filename):
    vector = []
    with open(filename, "r") as f:
        for line in f:
            cordinate = line.strip()
            cordinate = cordinate.split()
            cordinate[0] = int(cordinate[0])
            cordinate[1] = int(cordinate[1])
            vector += cordinate
    return vector

print(readPolygonFile("polygonFile.txt"))


