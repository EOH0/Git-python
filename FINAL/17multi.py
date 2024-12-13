def find_factors(n):
    # 숫자를 2부터 순차적으로 나누어보며 약수를 찾음
    i = 2
    while i * i <= n:  # i의 제곱이 n보다 작거나 같을 때까지만 탐색
        if n % i == 0:  # 나누어 떨어지면 i는 n의 약수
            return i, n // i  # i와 n을 i로 나눈 몫이 두 약수
        i += 1  # i를 1씩 증가시키며 다음 숫자 확인

    # 약수를 찾지 못하면, n 자체가 소수임
    return n, 1  # 소수인 경우 자기 자신과 1 반환

# 테스트 케이스
n1 = 756360141659
n2 = 111111111111111

a1, b1 = find_factors(n1)
print(f"{n1} -> {a1}, {b1}")

a2, b2 = find_factors(n2)
print(f"{n2} -> {a2}, {b2}")
