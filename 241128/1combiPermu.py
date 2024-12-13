def permu(a, ans, n):
    # n이 0이면 ans를 출력
    if n == 0:
        print(ans)
        return
    for i in range(len(a)):
        # ans에 a[i]를 추가하고, a에서 해당 값을 제거하여 재귀 호출
        ans1 = ans[:]
        a1 = a[:]
        ans1.append(a1.pop(i))  # a1에서 i번째 값을 제거
        permu(a1, ans1, n-1)

def combi(a, ans, n):
    # 길이가 3인 조합을 찾으면 출력
    if len(ans) == 3:
        print(ans, end = ", ")
        return
    # 조합의 길이가 3보다 작은 경우
    if len(a) + len(ans) < 3:
        return
    # 첫 번째 원소를 추가하여 재귀 호출
    ans1 = ans[:]
    ans1.append(a[0])
    combi(a[1:], ans1, n - 1)
    
    # 첫 번째 원소를 추가하지 않고 재귀 호출
    ans2 = ans[:]
    combi(a[1:], ans2, n)

if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    # 순열을 출력
    permu(a, [], len(a))
    print("+==================")
    # 길이가 3인 조합을 출력
    n = 3
    combi(a, [], n)
