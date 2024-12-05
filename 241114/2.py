if __name__ == "__main__":
    l = [4, 7, 1, 8, 3, 9, 9, 1, 4, 6, 8, 10]
    templ = l[:] # 무슨 차이지
    l.sort(reverse=True)
    templ.sort(reverse=True)
    # print(templ[4])
    # print(l[4]) # 다섯번째로 큰 값
    print(l)
    print(templ)
    # l.sort(reverse=True) # 크기 역순으로 (큰거 부터)