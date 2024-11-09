def fibo(n):
    if n == 1 or n == 2:
        return 1
    return fibo(n - 1) + fibo(n - 2)

if __name__ == "__main__":
    n = 10
    fibo_values = []  # 피보나치 수를 저장할 리스트

    # 피보나치 수열의 값을 리스트에 저장
    for i in range(1, n + 1):
        fibo_values.append(fibo(i))

    # print(fibo_values)  # 출력: [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    x = 8

    found = 0
    for i in range(len(fibo_values)):
        if x == fibo_values[i]:
            print("True")
            found = 1
            break
    if (found == 0):
        print("False")
