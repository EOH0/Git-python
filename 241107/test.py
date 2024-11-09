if __name__ == "__main1__":
    i = 1
    j = 13
    k = 1
    count = 0
    for n in range(i, j + 1):
        temp = str(n).count(str(k))
        count += temp
        if temp > 0:
            print(str(n), end=" ")
    print(" ")
    print(count)

if __name__ == "__main2__":
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

if __name__ == "__main__":
    a = "aabbbcccc"
    a = list(a)
    b = []
    b.append(a.pop(0))
    print(b, a)
    count = 1

    # 쉬운 방법
    for ch in a:
        if ch == b[-1]:
            count += 1
        else:
            if count > 1:
                b.append(str(count))
            b.append(ch)
            count = 1
    if count > 1:
        b.append(str(count))
    print(b)
    b = ' '.join(b)
    print(b)

    # 어려운 방법
    # while len(a) > 0:
    #     if b[-1] != a[0]:
    #         if count > 1:
    #             b.append(str(count))
    #         b.append(a.pop(0))
    #         count = 1
    #     else:
    #         while len(a) > 0 and b[-1] == a[0]:
    #             count += 1
    #             a.pop(0)
    # if count > 1:
    #     b.append(str(count))
    # b = " ".join(b)
    # print(b)
