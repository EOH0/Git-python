if __name__ == "__main__":
    a = [1,3,5,7,9]
    b = [2,3,6,7,8,9]
    c = []
    # ai = 0
    # bi = 0
    # while(ai != len(a) and bi != len(b)):
    #     if a[ai] < b[bi]:
    #         c.append(a[ai])
    #         ai += 1
    #     elif a[ai] == b[bi]:
    #         c.append(a[ai])
    #         c.append(b[bi])
    #         ai += 1
    #         bi += 1
    #     elif a[ai] > b[bi]:
    #         c.append(b[bi])
    #         bi += 1
    while (len(a) > 0 and len(b) > 0):
        if (a[0] < b[0]):
            c.append(a.pop(0))
        else:
            c.append(b.pop(0))
    if len(a) > 0:
        c.extend(a)
    else:
        c.extend(b)
    print(c)