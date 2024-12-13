if __name__ == "__main__":
    text = "programmers"
    alpha = [0] * 26
    for ch in text:
        alpha[ord(ch) - ord('a')] += 1
    print(alpha)