if __name__ == "__main__":
    n = 123  # 입력 받기
    sum_digits = 0  # 각 자리 숫자의 합

    # 숫자의 각 자리를 순차적으로 더하기
    for digit in n:
        sum_digits += int(digit)

    # 각 자리 숫자의 합을 9로 나눈 나머지 구하기
    result = sum_digits - (sum_digits // 9) * 9  # 나머지 연산자 %를 사용하지 않고 계산

    print(result)
