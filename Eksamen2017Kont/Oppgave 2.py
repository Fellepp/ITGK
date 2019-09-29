# a)
def file_to_list(filename):
    priceWar = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            line = line.split()
            priceWar.append(line)
    return priceWar


#dataList = file_to_list("pricewar.txt")
#print(dataList)


# b)
def list_stores(dataList):
    storeList = []
    for butikker in dataList:
        if butikker[0] not in storeList:
            storeList.append(butikker[0])
    return storeList


#storeList = list_stores(dataList)
#print(storeList)

# c)
def sum_prices_stores(dataList, storeList):
    sum = [0] * len(storeList)
    for i in range(len(dataList)):
        for j in range(len(storeList)):
            if dataList[i][0] == storeList[j]:
                sum[j] += float(dataList[i][2])
    return sum

#sumStores = sum_prices_stores(dataList, storeList)
#print(sumStores)

# d)
def rank_stores(storeList, sumStores):
    return [x for y, x in sorted(zip(sumStores, storeList))]

#sorted = rank_stores(storeList, sumStores)
#print(sorted)

# e)
def store_analysis(filename):
    dataList = file_to_list(filename)
    storeList = list_stores(dataList)
    sumStores = sum_prices_stores(dataList, storeList)
    storesRanked = rank_stores(storeList, sumStores)

    print("The total price for shopping per store is: ")
    for i in range(len(storeList)):
        print(storeList[i] + ": " + str(sumStores[i]) + " kr")
    print("\nThe ranking of stores according to prices is: ")
    for i in range(len(storesRanked)):
        print((i+1), storesRanked[i])

store_analysis("pricewar.txt")
