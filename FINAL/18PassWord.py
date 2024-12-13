if __name__ == "__main__":
    # 테스트 암호
    pw = "password" # False
    # pw = "Pa$$w5rd" # True
    # pw = "Pa$$w5r"  # False

    # 소문자, 대문자, 숫자, 특수문자 각각의 조건 리스트
    chrList = [
        "abcdefghijklmnopqrstuvwxyz",  # 소문자
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ",  # 대문자
        "0123456789",                 # 숫자
        "!@#$%^&*()-_=+[{]}|;:'\",<.>/?`~"  # 특수문자
    ]

    ans = True

    # 1. 암호 길이가 8 미만이면 조건 불충족
    if len(pw) < 8:
        ans = False

    # 2. 각각의 조건을 확인
    if ans:  # 길이가 충분한 경우에만 검증
        for chrs in chrList:  # 각 조건 리스트 검사
            temp = False
            for ch in pw:  # 암호의 각 문자에 대해
                if ch in chrs:  # 문자가 해당 조건 리스트에 있으면
                    temp = True
                    break
            if not temp:  # 해당 조건을 만족하는 문자가 없으면 실패
                ans = False
                break
    print(ans)
