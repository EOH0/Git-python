# 1522756 -> 1234
# 1524155677489  -> 1234567
# 2323050529221952581345121 -> 1524155677489
# 5396563761318393964062660689603780554533710504641 -> 2323050529221952581345121
if __name__ == "__main__":
    n = 1524155677489
    # n = 2323050529221952581345121
    # n = 5396563761318393964062660689603780554533710504641
    min = 1
    max = n
    while True:
        a = int((min + max) / 2)
        print(f"=============={a}")
        if (a * a == n):
            break
        elif (a * a > n):
            max = a - 1
        elif (a * a < n):
            min = a + 1
    print(a)