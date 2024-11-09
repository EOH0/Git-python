import random

if __name__ == "__main__":
    n = 20
    a = []
    for i in range(0, 5):
        num = random.randrange(1, n)
        a.append(num)
    a.sort()
    print(a)