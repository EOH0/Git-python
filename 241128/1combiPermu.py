def combi(a, ans, n):
    if (len(ans) == 3):
        print(ans, end = ", ")
        return
    if (len(a) + len(ans) < 3):
        return
    ans1 = ans[:]
    ans1.append(a[0])
    combi(a[1:], ans1, n - 1)
    ans2 = ans[:]
    combi(a[1:], ans2, n)

def permu(a, ans, n):
    if n == 0:
        print(ans)
        return
    for i in range(len(a)):
        ans1 = ans[:]
        a1 = a[:]
        ans1.append(a1.pop(i))
        permu(a1, ans1, n-1)

if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    permu(a, [], len(a))
    print("+==================")
    n = 3
    combi(a, [], n)