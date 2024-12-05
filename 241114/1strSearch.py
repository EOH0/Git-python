if __name__ == "__main__":
    # a = "banana"
    a = "banananananananana"
    b = "ana"

    count = 0
    idx = -1
    while True:
        idx = a.find(b, idx + 1)
        print(idx)
        if idx == -1:
            break
        else:
            count += 1
    print(count)

#     idx = a.find(b)
#     print(idx) # 인덱스 1에서 찾고자 하는 값이 시작

#     idx = a.find(b, idx+1)
#     print(idx) # 1 뒤에서 찾고자 하는 값이 시작하는 위치

#     idx = a.find(b, idx + 1)
#     print(idx) # 더 뒤에는 값이 없으므로 -1