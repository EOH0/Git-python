if __name__ == "__main__":
    aTuple = (1,2,3,4,5,6,7,8,9)
    if 8 in aTuple: # 8이 튜플안에 있으면
        print(aTuple.index(8)) # 8의 인덱스 출력

if __name__ == "__main12__":
    aTuple = (1,2,3,4,5,6,7,8,9)
    for i in range(len(aTuple)):
        print(aTuple)