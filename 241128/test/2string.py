def remove_adjacent_pairs(s):
    # 리스트로 변환하여 처리
    a = []  # 결과를 저장할 스택
    b = list(s)  # 입력 문자열을 리스트로 변환

    while True:
        if len(a) == 0 and len(b) != 0:
            a.append(b.pop(0))
        elif len(a) != 0 and len(b) != 0:
            if a[-1] == b[0]:
                a.pop(-1)  # 같은 문자 제거
                b.pop(0)   # 제거된 문자와 함께 다음 문자 제거
            else:
                a.append(b.pop(0))  # 다른 문자 추가
        else:
            break

    # 최종 결과 반환
    return 1 if len(a) == 0 else 0

if __name__ == "__main__":
    user_input = input("문자열을 입력하세요: ")
    result = remove_adjacent_pairs(user_input)
    print("결과:", result)
