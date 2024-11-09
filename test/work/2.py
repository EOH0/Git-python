def question1(str1):
    str1 = str(str1)
    str1 = str1.replace("    ", " ")
    print(str1)

def question2(a):
    sum = 0
    for i in range(len(a)):
        sum += a[i]
    avg = sum / len(a)
    print(int(avg))

def question3(num):
    numS = str(num)
    numOL = list(numS)
    
    numOL.sort(reverse=True)
    
    a = ''.join(numOL)
    a = int(a)
    print(a)

def question4(list1):
    max = 0
    for i in range(len(list1)):
        for j in range(i + 1, len(list1)):
            if (max <= list1[i] * list1[j]):
                max = list1[i] * list1[j]
    print(max)

def question5(a):
    n = 1
    cnt = 0
    for i in range(len(a)):
        if (n <= a[i]):
            cnt += 1
    print(cnt)

if __name__ == "__main__":
    str1 = "I    love    python"
    question1(str1)

    # a = [1, 6, 4, 3, 8, 8]
    # question2(a)

    # num = 118372
    # question3(num)

    # list1 = [4, 1, 7, 8, 3, 6]
    # # list2 = [-7, 4, 1, 7, -9, 8, -3, 6]
    # question4(list1)

    # a = [-7, 4, 1, 7, -9, 8, -3, 6]
    # question5(a)