def gen(text, length, n):
    for ch in chrs:
        text = text + ch
        if length > 1:
            gen(text, length-1, n)
        text = text[:-1]
        print(text)

if __name__ == "__main__":
    chrs = "abcdefghijklmnopqrstuvwxyz"
    for length in range(1, 9):
        gen("", length, 1)