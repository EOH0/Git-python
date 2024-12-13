if __name__ == "__main__":
    aList = [1, 2, 4, 5]
    n = 3
    minval = aList[0]
    minDiff = abs(aList[0] - n)
    for val in aList:
        print(abs(val - n))
        if minDiff > abs(val - n):
            minval = val
            minDiff = abs(val - n)
    print("answer: ", minval)