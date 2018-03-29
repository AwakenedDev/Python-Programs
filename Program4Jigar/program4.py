import datetime
monthDictionary = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October',
                 11: 'November', 12: 'December'}
def maxTemp(list):
    """
    Max temp reported by any WBAN's during August
    :param list:
    :return: in this method we return the string that has the information for Maximum Temperature (Output formatted report)
    """
    tempMax = 0
    counter = 0
    i = 0
    while (i < (len(list))): #in this while loop we iterate through every line in the list to find the max Temp
        string = str(list[i])
        string2 = string.split()
        if (int(string2[2]) > tempMax): #condition check
            tempMax = int(string2[2])
            counter = i
        i= i+1
    finalString = list[counter].split()
    tMax = finalString[2]
    date = datetime.datetime.strptime(str(finalString[1]), '%Y%m%d') #parse date
    dateM = monthDictionary[date.month]
    dateFinal = dateM + date.strftime(" %d, %y") #formats date
    stationName = finalString[5]
    locationName = finalString[6]
    return ("%-12s %-15s %-20s %-30s\n" % (tMax, dateFinal, stationName, locationName) )

def minTemp(list):
    """
    Min temp reported by any WBAN's during August 2015
    :param list:
    :return: in this method we return the string that has the information for Minimum Temperature (Output formatted report)
    """
    tempMin = 200
    counter = 0
    i = 0
    while (i < (len(list))): #in this while loop we iterate through every line in the list to find the min Temp
        string = str(list[i])
        string2 = string.split()
        if (int(string2[3]) < tempMin): #condition check
            tempMin = int(string2[3])
            counter = i
        i = i + 1
    finalString = list[counter].split()
    tMin = finalString[3]
    date = datetime.datetime.strptime(str(finalString[1]), '%Y%m%d') #parse date
    dateM = monthDictionary[date.month]
    dateFinal = dateM + date.strftime(" %d, %y") #formats date
    stationName = finalString[5]
    locationName = finalString[6]
    return ("%-12s %-15s %-20s %-30s\n" % (tMin, dateFinal, stationName, locationName))

def avgTemp(list):
    """
    The average average (Tavg) temperature for all 25 reporting stations in August 2015
    :param list:
    :return: in this method we return the value of average TAvg
    """
    avgSum = 0
    i = 0
    while (i < (len(list))): #condition check and calculation
        string = str(list[i])
        string2 = string.split()
        avgSum = avgSum + int(string2[4])
        i = i + 1
    totalNum = (len(list)-1)
    avgTempAll = (avgSum / totalNum)
    return avgTempAll

def hotDay(list):
    """
    The hottest day in Pennsylvania in August 2015
    :param list:
    :return: in this method we return the list that has information of the hottest day in Pennsylvania
    """
    list2 = []
    list3 = []
    i = 0
    while (i < (len(list))): #in this while loop we extract the Data and Tavg info and then store it in list2
        string = str(list[i])
        string2 = string.split()
        finalst = str(string2[1]) + " " + str(string2[2])
        list2.insert(i, finalst)
        i = i +1
    list2.sort() #After storing the Date and Tmax, we sort the data in lis2t.
    global  avgTmax, counter, j, l, k
    avgTmax = 0
    j = 0
    k = 0
    m = 0
    counter  = 0
    l = 1
    while (j < (len(list2))): #here we iterate through each index (line) of list 2 and calculate average Tmax for each day
        string = str(list2[j])
        string2 = string.split()
        if (l < len(list2)) :
            stringAhead = str(list2[l])
            stringAhead2 = stringAhead.split()
            if not (int(string2[0]) == int(stringAhead2[0])): #here is the condition to see if the dates are same. If dates are the same, add the temp, when dates are not same, calculate average.
                #remember since list2 is sorted, the dates in the list are also sorted meaning the same date's value will be adjacent untill a certain index, then the next day's values are presented
                counter = j
                counter = counter - k
                k=j
                avgTmax = avgTmax + int(string2[1]) #add all same date's vaues
                avgT = avgTmax/(counter)#calculate average
                hotDayTemp = (str(string2[0]) + " " + str(float(avgT)))
                list3.insert(m, hotDayTemp)
                avgTmax = 0 #prepare for next days' values
            else:
                avgTmax = avgTmax + int(string2[1]) #if dates are same do this
        j=j+1
        l=l+1
        m=m+1
    avgtempMax = 0.0
    maxCounter = 0
    n = 0
    while (n < (len(list3))): #in this loop we find the hottest day by comparing average of Tmax for each day
        string = str(list3[n])
        string2 = string.split()
        if (float(string2[1]) > avgtempMax): #condition check
            avgtempMax = float(string2[1])
            maxCounter = n
        n = n + 1
    finalString = list3[maxCounter].split()
    avgFinalTmax = finalString[1]
    date = datetime.datetime.strptime(str(finalString[0]), '%Y%m%d') #parse date
    dateM = monthDictionary[date.month]
    dateFinal = dateM + date.strftime(" %d, %y") #format date
    list4 = [dateFinal, avgFinalTmax]
    return list4

def coldDay(list):
    """
    The coldest day in Pennsylvania in August 2015
    :param list:
    :return: in this method we return the list that has information of the coldest day in Pennsylvania
    """
    list2 = []
    list3 = []
    i = 0
    while (i < (len(list))): #in this while loop we extract the Data and Tavg info and then store it in list2
        string = str(list[i])
        string2 = string.split()
        finalst = str(string2[1]) + " " + str(string2[3])
        list2.insert(i, finalst)
        i = i +1
    list2.sort() #After storing the Date and Tmin, we sort the data in lis2t.
    global  avgTmax, counter, j, l, k
    avgTmax = 0
    j = 0
    k = 0
    m = 0
    counter  = 0
    l = 1
    while (j < (len(list2))): #here we iterate through each index (line) of list 2 and calculate average Tmin for each day
        string = str(list2[j])
        string2 = string.split()
        if (l < len(list2)) :
            stringAhead = str(list2[l])
            stringAhead2 = stringAhead.split()
            if not (int(string2[0]) == int(stringAhead2[0])):#here is the condition to see if the dates are same. If dates are the same, add the temp, when dates are not same, calculate average.
                #remember since list2 is sorted, the dates in the list are also sorted meaning the same date's value will be adjacent untill a certain index, then the next day's values are presented
                counter = j
                counter = counter - k
                k=j
                avgTmax = avgTmax + int(string2[1])#add all same date's vaues
                avgT = avgTmax/(counter)#calculate average
                hotDayTemp = (str(string2[0]) + " " + str(float(avgT)))
                list3.insert(m, hotDayTemp)
                avgTmax = 0 #prepare for next days' values
            else:
                avgTmax = avgTmax + int(string2[1])#if dates are same do this
        j=j+1
        l=l+1
        m=m+1
    avgtempMin = 200.0
    minCounter = 0
    n = 0
    while (n < (len(list3))):#in this loop we find the hottest day by comparing average of Tmax for each day
        string = str(list3[n])
        string2 = string.split()
        if (float(string2[1]) < avgtempMin):
            avgtempMin = float(string2[1])
            minCounter = n
        n = n + 1
    finalString = list3[minCounter].split()
    avgFinalTmax = finalString[1]
    date = datetime.datetime.strptime(str(finalString[0]), '%Y%m%d') #parse date
    dateM = monthDictionary[date.month]
    dateFinal = dateM + date.strftime(" %d, %y") #format date
    list4 = [dateFinal, avgFinalTmax]
    return list4

def main():
    """
    This class has methods that creates an ArrayList of WbanRecords, reads the weather data then uses the Array list data to produce 5 reports
    """
    file = input("\nEnter the filename: ")
    #file = "tempData2015.txt" - (this was for quick testing)
    list = []
    numLines = 0
    try:

        f = open(file, "r")
        for line in f: #count the number of lines presn in the file. Number of lines will be the length of the list
            numLines = numLines + 1
        f.close()
    except FileNotFoundError:
        pass

    try:
        #with open(file, "r") as f: #open the file and store it in a list
        f = open(file, "r")
        i = 0
        while(i<(numLines)):
            list.insert(i, str(f.readline()))
            i=i+1

        tMax = maxTemp(list) #prints maxTemp info
        print("\n1. Maximum temperature reported by any of the WBAN's during August is ")
        print("\n%-12s %-15s %-20s %-30s" % ("MaxTemp(F)", "Date", "Station", "Location"))
        print("--------------------------------------------------------------------------------------------")
        print((tMax))

        tMin = minTemp(list)#prints minTemp info
        print("\n2. Minimum temperature reported by any of the WBAN's during August is ")
        print("\n%-12s %-15s %-20s %-30s" % ("MinTemp(F)", "Date", "Station", "Location"))
        print("--------------------------------------------------------------------------------------------")
        print(tMin)

        tAvg = avgTemp(list)#prints sverageTemp info
        print("\n3. Average average temperature for all 25 reporting was %i Fahrenheit" % (tAvg))

        avgTmax = hotDay(list)#prints hottest day info
        print("\n4. The hottest day in Pennsylvania was on %s with average temperature of %.2f Fahrenheit" % (str(avgTmax[0]), float(avgTmax[1])))

        avgTmin = coldDay(list)#printcoldest day info
        print("\n5. The coldest day in Pennsylvania was on %s with average temperature of %.2f Fahrenheit" % (str(avgTmin[0]), float(avgTmin[1])))

        f.close()
    except FileNotFoundError:
        print("Error: File not Found")

if __name__ == "__main__":
    main()