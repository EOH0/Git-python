if __name__ == "__main__":
    a = [[1, 1], [3, 1], [3, 4], [1, 4]]
    p1 = a[0]
    p2 = a[0]

    for i in range(1, len(a)):
        if sum(p1) > sum(a[i]):
            p1 = a[i]
        if sum(p2) < sum(a[i]):
            p2 = a[i]
        print(i)
    print(p1, p2)
    print((p2[0] - p1[0]) * (p2[1] - p1[1]))