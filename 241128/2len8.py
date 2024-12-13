def gen(text, length, n):
    # 길이가 0이면 텍스트 출력
    if length == 0:
        print(text)
        return

    # 문자를 하나씩 더해서 재귀 호출
    for ch in chrs:
        gen(text + ch, length - 1, n)

if __name__ == "__main__":
    chrs = "abcdefghijklmnopqrstuvwxyz"
    # 길이가 1부터 8까지인 모든 문자열을 생성
    for length in range(1, 9):
        gen("", length, 1)
