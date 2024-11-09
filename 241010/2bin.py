if __name__ == "__main2__" :
    a = "1001"
    b = "1111"
    print(bin(int(a, 2) + int (b, 2))[2:])

if __name__ == "__main__" :
    n1 = int(input(), 2)
    n2 = int(input(), 2)

    sum = n1 + n2

    print(bin(sum)[2:])