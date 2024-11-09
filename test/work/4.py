import random

def question3(a):
    sum = ""
    i = 0
    while(i < len(a)):
        if a[i:i+4] == 'zero':
            sum += '0'
            i += 4
        elif a[i:i+3] == 'one':
            sum += '1'
            i += 3
        elif a[i:i+3] == 'two':
            sum += '2'
            i += 3
        elif a[i:i+5] == 'three':
            sum += '3'
            i += 5
        elif a[i:i+4] == 'four':
            sum += '4'
            i += 4
        elif a[i:i+4] == 'five':
            sum += '5'
            i += 4
        elif a[i:i+3] == 'six':
            sum += '6'
            i += 3
        elif a[i:i+5] == 'seven':
            sum += '7'
            i += 5
        elif a[i:i+5] == 'eight':
            sum += '8'
            i += 5
        elif a[i:i+4] == 'nine':
            sum += '9'
            i += 4    
    print(sum)

def fibo(n):
    if n == 1 or n == 2:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)

def question4(a):
    L = []
    n = 25
    for i in range(1, n):
        L.append(fibo(i))

    flag = 0
    for i in range(len(L)):
        if (a == L[i]):
            flag = 1

    print(L)

    if(flag):
        print("True")
    else:
        print("False")

def question5(a, L):
    cnt = 0
    for i in range(len(L)):
        if (a < L[i]):
            cnt += 1
    print(cnt)
    
def question6(oct1, oct2):
    print(oct1, oct2)
    sum = oct1 + oct2
    print(oct(sum)[2:]) # 10진수를 다시 8진수로

def question7(a):

    num = [ 0 ] * 26 # 초기화하고 배열 개수 26개로 늘려주기
    for i in range(len(a)):
        j = (ord(a[i]) - ord('a'))
        num[j] += 1
    print(num)

def question8(L2D):
    sum = 0
    max = 0
    for i in range(len(L2D)):
        for j in range(len(L2D[i])):
            if (max <= L2D[i][j]):
                max = L2D[i][j]
            sum += L2D[i][j]
    print(sum, max)

def question9():
    n = int(input())
    L = list(range(1, n + 1))

    random.shuffle(L)

    print(L[:5])
    

if __name__ == "__main__":
    # a = 'onetwothree'
    # question3(a)

    # a = int(input())
    # question4(a)

    # a = int(input())
    # L = [1, 2, 3, 4, 5, 6, 7, 8]
    # question5(a, L)

    # oct1 = int(input(), 8) # 8진수를 10진수로 자동으로 변경
    # oct2 = int(input(), 8)
    # question6(oct1, oct2)

    # a = "abcdefghijklmnopqrstuvwxyz"
    # question7(a)

    # L2D = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # question8(L2D)

    question9()