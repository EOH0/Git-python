if __name__ == "__main__":
    a = "aabbbcccc"
    a = list(a)
    b = []
    b.append(a.pop(0))
    print(b, a)
    count = 1

    # 쉬운 방법
    for ch in a:
        if ch == b[-1]:
            count += 1
        else:
            if count > 1:
                b.append(str(count))
            b.append(ch)
            count = 1
    if count > 1:
        b.append(str(count))
    print(b)
    b = ' '.join(b)
    print(b)