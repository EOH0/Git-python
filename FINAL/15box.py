if __name__ == "__main__":
    # [10, 8, 6], n = 3  -> 12
    # [10, 8, 7], n = 2  -> 60

    a = [10, 8, 6]
    n = 3
    # a = [10, 8, 7]
    # n = 2

    for i in range(len(a)):
        a[i] = int(a[i] / n)
    print(a)
    print(a[0] * a[1] * a[2])