if __name__ == "__main__":
    n = 2
    i = 0
    hap = 0

    for i in range(1, 101):
        i += 1
        if i % n != 0:
            continue
        hap += i
    print(hap)

if __name__ == "__main2__":
    n = 2
    i = 0
    hap = 0

    while i < 100:
        i += 1
        if i % n != 0:
            continue
        hap += i
    print(hap)