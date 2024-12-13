def generate_numbers_with_rule(l, r):
    numbers = [5]  # 시작값
    idx = 0
    result = []

    while True:
        current = numbers[idx]  # 현재 숫자
        # 새로 생성할 숫자
        next1 = current * 10  # 끝에 0을 추가
        next2 = current * 10 + 5  # 끝에 5를 추가

        # 범위를 벗어나면 중단
        if next1 > r and next2 > r:
            break

        # 범위 안에 들어오는 숫자만 추가
        if next1 <= r:
            numbers.append(next1)
        if next2 <= r:
            numbers.append(next2)

        idx += 1  # 다음 숫자로 이동

    # 최종적으로 l 이상 r 이하인 숫자만 필터링
    for num in numbers:
        if l <= num <= r:
            result.append(num)

    return result


if __name__ == "__main__":
    # 입력 범위
    l, r = 5, 555
    # l, r = 3, 1000000000

    # 결과 계산
    result = generate_numbers_with_rule(l, r)
    print(f"배열: {result}")
    print(f"배열의 길이: {len(result)}")
