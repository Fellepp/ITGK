weatherData = [
    [12.0, 2.4, 8.2],
    [6.1, 0.6, 11.9],
    [8.3, -3.5, 0.0],
    [11.6, -5.2, 0.0],
    [15.3, 2.8, 14.3]]


# a)
def weatherStats(weatherData):
    days = len(weatherData)
    highestTemp = 0
    lowestTemp = 0
    totalRain = 0

    for i in range(days):
        if weatherData[i][0] > highestTemp:
            highestTemp = weatherData[i][0]
            highestTempDay = i + 1
        elif weatherData[i][1] < lowestTemp:
            lowestTemp = weatherData[i][1]
            lowestTempDay = i + 1
        totalRain += weatherData[i][2]

    print("There are", days, "days in the period.")
    print("The highest temperature was", highestTemp, "C on day number", highestTempDay)
    print("The lowest temperatur was", lowestTemp, "C on day number", lowestTempDay)
    print("There was a total of", round(totalRain, 2), "mm rain in the period")


weatherStats(weatherData)


# b)
def coldestThreeDays(weatherData):
    lowestAverage = 0
    for i in range(0, len(weatherData) - 2):
        avg = (weatherData[i][1] + weatherData[i + 1][1] + weatherData[i + 2][1]) / 3
        if avg <= lowestAverage:
            lowestAverage = avg
            startday = i+1
    return startday

print(coldestThreeDays(weatherData))

# c)
def addNewDay(extraData, weatherData):
    newData = ""
    for i in extraData:
        if i in (".1234567890"):
            newData += i
        elif i in (","):
            newData += " "
    newData = newData.split()
    for i in range(0, len(newData)):
        newData[i] = float(newData[i])
    weatherData.append(newData)
    return weatherData

extraDate = "max=23.5, min=9.3, 5.1mm"
updated = addNewDay(extraDate, weatherData)
for line in updated:
    print(line)
