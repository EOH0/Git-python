def gen50(num, l, r, ans):
    if (int(num) > r):
        return
    if (l <= int(num)):
        ans.append(num)
    print(num)
    gen50(num + '0', l, r, ans)
    gen50(num + '5', l, r, ans)

if __name__ == "__main__":
    l = 3
    r = 1000000000
    num = '5'
    ans = []

    if l <= int(num) <= r:
        ans.append(num)
    gen50(num + '0', l, r, ans)
    gen50(num + '5', l, r, ans)
    for i in range(len(ans)):
        ans[i] = int(ans[i])
    print(ans)
    ans.sort()
    print(ans)
    print(len(ans))