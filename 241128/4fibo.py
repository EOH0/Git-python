# def fibo(n):
#     if n <= 1:
#         return n
#     return fibo(n - 1) + fibo(n - 2)

# for i in range(50):
#     print(fibo(i), end=" ")

def fibo(n): # 권장
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# 테스트
for i in range(50):
    print(fibo(i), end=" ") 