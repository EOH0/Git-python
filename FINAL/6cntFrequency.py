if __name__ == "__main__":
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