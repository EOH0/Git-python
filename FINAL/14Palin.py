if __name__ == "__main__":
# "A man, a plan, a canal: Panama" -> True
# "A man, a plan, canal: Panama" -> False
# "다시 합창합시다."  -> True
    a = "A man, a plan, a canal: Panama"
    b = []
    for ch in a:
        if ch.isalpha():
            b.append(ch.lower())
    print(b)
    while len(b) > 1:
        if b[0] == b[-1]:
            b.pop(0)
            b.pop(-1)
        else:
            break
    print(b)
    if len(b) <= 1:
        print(True)
    else:
        print(False)