if __name__ == "__main1__":
    a = [4, 1, 7, 8, 3, 6]
    b = [-7, 4, 1, 7, -9, 8, -3, 6]

    i = 0
    amax = 0
    amult = 0
    for i in range(0, len(a)):
        for j in range(i + 1, len(a)):
            amult = a[i] * a[j]
            if amax < amult:
                amax = amult

    bmax = 0
    bmult = 0
    for i in range(0, len(b)):
        for j in range(i + 1, len(b)):
            bmult = b[i] * b[j]
            if bmax < bmult:
                bmax = bmult

    print(amax, bmax)
    
if __name__ == "__main__":
    a = [4, 1, 7, 8, 3, 6]
    a.sort()
    print(a[0]*a[1], a[len(a)-2]*a[len(a)-1])