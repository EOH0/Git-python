if __name__ == "__main__":
    a = 118372
    print(''.join(list(str(a)).sort(reverse=True)))


if __name__ == "__main3__":
    a = 118372
    a = str(a)
    a = list(a)
    a.sort(reverse=True)
    a = ''.join(a)
    a = int(a)
    print(a, type(a))
    
if __name__ == "__main2__":
    n = list(input())
    n.sort(reverse=True)

    for i in range(0, len(n)):
        print(n[i], end='')

