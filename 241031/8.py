def findAns(a, num):
    txt = ""
    for char in a:
        if char.isalpha():  # 문자일 때만 처리
            if char.isupper():  # 대문자
                txt += chr((ord(char) - ord('A') - num) % 26 + ord('A'))
            else:  # 소문자
                txt += chr((ord(char) - ord('a') - num) % 26 + ord('a'))
        else:
            txt += char  # 알파벳이 아닌 경우 그대로 추가
    return txt

if __name__ == "__main__":
    a = "AbclgPizlIvlJmIujqbqwca"
    # 가능한 num를 모두 확인
    for num in range(1, 26):
        print(f"num {num}: {findAns(a, num)}")
