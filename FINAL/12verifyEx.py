if __name__ == "__main__":
    # eval, split 사용법 정확히 알고 활용하기
    a = ["19 - 6 = 13",  "5 + 66 = 71",  "5 - 15 = 63",  "3 - 1 = 2"]
    for item in a:
        spl = item.split("=")
        if eval(spl[0]) == eval(spl[1]):
            print(item, ": O")
        else:
            print(item, ": X")