if __name__ == "__main__":
    a = 78720646226947352489
    while True:
        hap = 0
        a = str(a)
        for ch in a:
            hap += int(ch)
        print(hap)
        if hap >= 9:
            a = str(hap)
        else:
            print(hap)
            break
        