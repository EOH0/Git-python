if __name__ == "__main__":
    # pw = "password" # False
    # Pa$$w5rd # True
    pw =  "Pa$$w5r" # False
    # chrList = [#소문자 대문자 숫자 특수기호]
    ans = True
    if len(pw) < 8:
        ans = False
    print(ans)
    # if ans == True:
    #     for chrs in chrList:
    #         temp = False
    #         for ch in pw:
    #             temp = True
    #             break
    #         if temp == False:
    #             ans = False
    #             break
    print(ans)