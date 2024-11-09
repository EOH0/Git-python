if __name__ == "__main__":
    a = [-7, 4, 1, 7, -9, 8, -3, 6]

    n = int(input())
    comp = 0
    for i in range(0, len(a)):
        if (n > a[i]):
            comp += 1
    comp = len(a) - comp
    print(comp)
