# a)
def readTime():
    hour = int(input("Enter hour: "))
    while (hour not in range(0, 24)):
        print("ERROR: Hour must be between 0 and 23!")
        hour = int(input("Enter hour: "))
    minute = int(input("Enter minute: "))
    while (minute not in range(0, 59)):
        print("ERROR: Minute must be between 0 and 59!")
        minute = int(input("Enter hour: "))
    second = int(input("Enter second: "))
    while (second not in range(0, 59)):
        print("ERROR: Second must be between 0 and 59!")
        second = int(input("Enter second: "))
    return [hour, minute, second]


# print(readTime())

# b)
def convertTime(time, mode):
    if mode == "time":
        hour = time // 3600
        minute = (time % 3600) // 60
        second = (time % 60)
        return [hour, minute, second]
    elif mode == "sec":
        second = time[0] * 3600 + time[1] * 60 + time[2]
        return second


print(convertTime([1, 4, 17], "sec"))


# c)
def travelTime():
    print("Give departure time in hour, minute and second: ")
    departure = readTime()

    print("Give arrival time in hour, minute and second: ")
    arrival = readTime()
    while (departure[0] > arrival[0] or (departure[0] == arrival[0] and (departure[1] > arrival[1]) or (
                    departure[1] == arrival[1] and departure[2] > arrival[2]))):
        print("ERROR: Arrival time must be later than Departure time")
        print("Give arrival time in hour, minute and second: ")
        arrival = readTime()
    travelTime = convertTime(arrival, "sec") - convertTime(departure, "sec")
    travelTime = convertTime(travelTime, "time")
    print("Traveltime:", travelTime[0], "hours,", travelTime[1], "minutes", travelTime[2], "seconds")


# travelTime()


# b)
def travelTime(departure, arrival):
    departure.append(0)
    arrival.append(0)
    travelTime = convertTime(arrival, "sec") - convertTime(departure, "sec")
    return convertTime(travelTime, "time")


def analyzeBusRoutes(busTables):
    # [nr, starttid, stopptid]
    fastestTime = travelTime([busTables[0][1], busTables[0][2]], [busTables[0][3], busTables[0][4]])
    slowestTime = travelTime([busTables[0][1], busTables[0][2]], [busTables[0][3], busTables[0][4]])
    fastestBus = busTables[0][0]
    shortestBus = busTables[0][0]
    for i in range(0, len(busTables)):
        if travelTime([busTables[i][1], busTables[i][2]], [busTables[i][3], busTables[i][4]]) < fastestTime:
            fastestTime = travelTime([busTables[i][1], busTables[i][2]], [busTables[i][3], busTables[i][4]])
            fastestBus = busTables[i][0]
        elif travelTime([busTables[i][1], busTables[i][2]], [busTables[i][3], busTables[i][4]]) > slowestTime:
            slowestTime = travelTime([busTables[i][1], busTables[i][2]], [busTables[i][3], busTables[i][4]])
            slowestBus = busTables[i][0]
    print("The slowest bus route is bus nr.", slowestBus, "and it takes", slowestTime[0], "hour,", slowestTime[1],
          "min.")
    print("The fastest bus route is bus nr.", fastestBus, "and it takes", fastestTime[0], "hour,", fastestTime[1],
          "min.")


Busses = [[1, 15, 0, 15, 19],
          [3, 15, 32, 16, 45],
          [4, 15, 45, 16, 23],
          [5, 15, 55, 16, 11]]

analyzeBusRoutes(Busses)
