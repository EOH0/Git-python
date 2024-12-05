import math

def isPrime(n):
    # for i in range(2, n) :
    #     if n % i == 0:
    #         return False
    # return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    n = 1024 * 1024
    print(int(math.sqrt(n)) + 1)
    ans = []
    for i in range(2, int(n + 1)):
        if n % i == 0 and isPrime(i):
            ans.append(i)
    print(ans)