if  __name__ == "__main16__":
    aStr = "asdlkajv2109!#$voiasjdv!#oia"
    bStr = ""
    for i in range(len(aStr)):
        if aStr[i].isalnum():
            bStr += aStr[i]
        else :
            bStr += " "
    print(bStr)

if  __name__ == "__main6__":
    aStr = "abcedi31i3d1039dj3f03"
    outStr = ""
    for i in range(len(aStr)):
        if aStr[i].isnumeric():
            outStr += aStr[i]
        else :
            outStr += " "
    print(outStr)
    aList = outStr.split()
    print(aList)

if  __name__ == "__main__":
    aStr = "a       b       c        d       e        f       g" # split하고 다시 int화하기?
    aList = aStr.split()
    print(aList)
    bstr = ":w".join(aList)
    print(bstr)
    # while True:
    #     bStr = aStr.replace(" ", "")
    #     if len(bStr) == len(aStr):
    #         break
    # print(bStr)

if  __name__ == "__main4__":
    aStr = "a b c d e f g"
    print(aStr)
    bStr = aStr.replace(" ", "")
    print(bStr)

if  __name__ == "__main3__":
    aStr = "abcdefg"
    print(aStr)
    bStr = aStr.replace("a", "A")
    print(bStr)

if  __name__ == "__main12__":
    aStr = "abcdefg"
    print(aStr)
    for i in range(len(aStr)):
        print(aStr[i])
    aStr = 'A' + aStr[1:]
    # bStr = 'A' + aStr[1:]
    print(aStr)