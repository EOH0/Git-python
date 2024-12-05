import hashlib

# 대상 MD5 해시
target_hash = "755f85c2723bb39381c7379a604160d8"

def gen(text, length, n):
    for ch in chrs:
        text = text + ch
        md5Text = hashlib.md5(text.encode()).hexdigest()
        if md5Text == target_hash:  # 대상 해시와 비교
            print(f"패스워드 찾음: {text}")  # 패스워드 출력
            exit()
        if length > 1:
            gen(text, length - 1, n)
        text = text[:-1]  # 마지막 문자 제거

if __name__ == "__main__":
    chrs = "abcdefghijklmnopqrstuvwxyz"  # 영문자만 사용
    for length in range(1, 9):  # 최대 길이 8까지 시도
        gen("", length, 1)
