if __name__ == "__main1__": # 모든 요소의 개수가 두개인만 작동하는 코드
    a = [[80, 70], [90, 50], [40, 70], [50, 80]]
    for i in range(len(a)):
        a[i]= a[i][0] + a[i][1]
    b = a[:]
    b.sort(reverse=True)
    ans = []
    for i in range(len(a)):
        ans.append(b.index(a[i]) + 1)
    print(ans)
if __name__ == "__main__": # 모든 요소의 개수가 다를때 작동하는 코드
    a = [[80, 70], [90, 50, 40], [40, 70, 20], [50, 80]]
    for i in range(len(a)):
        a[i]= sum(a[i]) / len(a[i])
    b = a[:]
    b.sort(reverse=True)
    ans = []
    for i in range(len(a)):
        ans.append(b.index(a[i]) + 1)
    print(ans)
    