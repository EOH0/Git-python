import math

def question1(num):
    sum = 0
    while (num > 1):
        sum += num % 10
        num = num // 10
    print(sum)

def question2(num1):
    flag = 1
    for i in range(2, num1):
        if (num1 % i == 0):
            print("소수 아님")
            flag = 0
            break
    if (flag):
        print("소수")

def question3(a, b):
    cnt = 0
    for i in range(len(a)):
        for j in range(len(b)):
            if (a[i] == b[j]):
                cnt += 1
    print(cnt)

def question4(a):
    result = ""
    for i in range(len(a)):
        if (str(a[i]).isalpha()):
            result += " "
        else:
            result += a[i]
    result = result.split()
    sum = 0
    for i in range(len(result)):
        sum += int(result[i])
    print(result, sum)

def question5(a, L):
    a = list(a)
    for i in L:
        a[i] = ""
    a = "".join(a)

    print(a)

def question7():
    n = int(input())

    pieces = math.lcm(6, n) / 6

    print(int(pieces))

if __name__ == "__main__":
    # num = 698142
    # question1(num)

    # num1 = int(input())
    # question2(num1)

    # a = [15, 4, 9, 3, 5]
    # b = [2, 8, 1, 0, 32, 9, 3]
    # question3(a, b)

    # a = "ab12c5d1e9"
    # question4(a)

    # a = "apporoograpemmemprs"
    # L = [1, 16, 6, 15, 0, 10, 11, 3]
    # question5(a, L)

    question7()