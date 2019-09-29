def is_leap_year ( year ):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False

def weekday_newyear0(year, end):
    teller1 = 1
    for i in range(year, end+1):
        if i !=year:
            year = year+teller1
        if year > 1900:
            ukedager = ["man", "tirs", "ons", "tors", "fre", "lør", "søn"]
            year1 = 1900
            year2 = year
        elif year < 1900:
            ukedager = ["man", "søn", "lør", "fre", "tors", "ons", "tirs"]
            year1 = year
            year2 = 1900
        else:
            ukedager = ["man"]
            year1 = year
            year2 = year

        ukedag = ukedager[teller(year1, year2)]
        print(year, ukedag)

def weekday_newyear(year):
    if year > 1900:
        ukedager = ["man", "tirs", "ons", "tors", "fre", "lør", "søn"]
        year1 = 1900
        year2 = year
    elif year < 1900:
        ukedager = ["man", "søn", "lør", "fre", "tors", "ons", "tirs"]
        year1 = year
        year2 = 1900
    else:
        ukedager = ["man"]
        year1 = year
        year2 = year

    ukedag = ukedager[teller(year1, year2)]
    return teller(year1, year2)


def teller(year1, year2):
    verdi = 0
    for i in range(year1, year2):
        if(is_leap_year(i)):
            verdi += 2
        else:
            verdi += 1
        if verdi>6:
            verdi %= 7
    return verdi

def is_workday(day):
    if day > 4:
        return False
    else:
        return True

def workdays_in_year(year):
    dager = 365
    if(is_leap_year(year)):
        dager = 366
    arbeidsdager=0
    dageTeller = weekday_newyear(year)
    for i in range(dager):
        dageTeller += 1
        if dageTeller > 6:
            dageTeller = 0
        if(is_workday(dageTeller)):
            arbeidsdager+=1
    return arbeidsdager

år = int(input("Fra år : "))
end = int(input("Tl og med: "))
weekday_newyear0(år, end)

for i in range(år, end):
    print(i,": ", workdays_in_year(i))