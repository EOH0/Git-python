if __name__ == "__main__":
    inTime = "12:25:33"
    ouTime = "13:30:50"
    inTimeList = inTime.split(":")
    print(inTimeList)
    for i in range(len(inTimeList)):
        inTimeList[i] = int(inTimeList[i])
    print(inTimeList)