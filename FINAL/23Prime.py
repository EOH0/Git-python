if __name__ == "__main__":
    n = 12  # 소인수 분해할 숫자
    result = []

    # 2부터 n까지의 수로 나누어 보면서 소인수 찾기
    i = 2
    while i * i <= n:  # i가 n의 제곱근을 넘지 않도록
        if n % i == 0:  # i로 나누어지면 소인수로 추가
            result.append(i)
            while n % i == 0:  # 중복된 i를 모두 나눠줌
                n //= i
        i += 1  # i 증가

    # 마지막에 남은 n이 소수라면 그 자체도 소인수
    if n > 1:
        result.append(n)

    print(result)
