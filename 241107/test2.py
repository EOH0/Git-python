if __name__ == "__main__":
    a = "ilovepython"
    b = "vnioheplytor"
    a = list(a)
    b = list(b)
    if len(a) != len(b):
        print(0)
    while (len(a) > 0):
        if a[0] in b:
            b.remove(a[0])
            a.pop(0)
        else:
            break
        print("a =", a, ", b =", b)
    if len(a) == 0 and len(b) == 0:
        print(1)
    else:
        print(0)