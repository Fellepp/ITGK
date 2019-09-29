#a
def summerOlympics(firstYear, lastYear):
    start = 1948
    if start > firstYear:
        return "The year needs to be >= 1948"
    years = []
    for i in range(firstYear, lastYear+1):
        if abs(i - start) % 4 == 0:
            years.append(i)
    return years

print(summerOlympics(1948, 3000))

#b
def findAge(bYear, bMonth, bDay):
    #(yyyy, mm, dd) = current_date()
    yyyy = 2017
    mm = 12
    dd = 8
    age = abs(bYear-yyyy)
    if mm > bMonth:
        age = age-1
    elif mm == bMonth and bDay < dd:
        age = age-1
    return age

print(findAge(1997, 12, 7))

#c)
def printAgeDiff(table):
    for i in range(0, len(table)-1):
        if findAge(table[i][2], table[i][3], table[i][4]) > findAge(table[i+1][2], table[i+1][3], table[i+1][4]):
            print(table[i][0], table[i][1], "is older than", table[i+1][0], table[i+1][1])
        elif findAge(table[i][2], table[i][3], table[i][4]) < findAge(table[i+1][2], table[i+1][3], table[i+1][4]):
            print(table[i][0], table[i][1], "is younger than", table[i + 1][0], table[i + 1][1])
        elif findAge(table[i][2], table[i][3], table[i][4]) == findAge(table[i+1][2], table[i+1][3], table[i+1][4]):
            print(table[i][0], table[i][1], "is at the same age as", table[i + 1][0], table[i + 1][1])

table=[['Justin','Bieber',1994,3,1],
 ['Donald','Duck',1934,8,1],
 ['George','Clooney',1961,5,6],
 ['Eddie','Murphy',1961,4,3]]

printAgeDiff(table)