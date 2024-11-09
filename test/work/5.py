def question1(a,b):
    c = a + b
    print(bin(c)[2:])


if __name__ == "__main__":
    a = input() 
    b = input()
    a1 = int(a, 8)
    b1 = int(b, 8)
    question1(a1,b1)