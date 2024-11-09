if __name__ == "__main__":
    s = "onetwothreezerofivesixseven"
    result = ''
    i = 0
    while i < len(s):
        # 각 숫자 이름의 길이에 따라 확인
        if s[i:i+4] == "zero": # s[i:i+4] == i ~ (i + 3)
            result += '0'
            i += 4
        elif s[i:i+3] == "one": # s[i:i+3] == i ~ (i + 2)
            result += '1'
            i += 3
        elif s[i:i+3] == "two":
            result += '2'
            i += 3
        elif s[i:i+5] == "three":
            result += '3'
            i += 5
        elif s[i:i+4] == "four":
            result += '4'
            i += 4
        elif s[i:i+4] == "five":
            result += '5'
            i += 4
        elif s[i:i+3] == "six":
            result += '6'
            i += 3
        elif s[i:i+5] == "seven":
            result += '7'
            i += 5
        elif s[i:i+5] == "eight":
            result += '8'
            i += 5
        elif s[i:i+4] == "nine":
            result += '9'
            i += 4
        else:
            i += 1  # 잘못된 부분이 있을 경우 다음 문자로 이동
    print(result)