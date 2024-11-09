if __name__ == "__main__":
    # 8진수로 입력받아 10진수로 변환
    oct1 = int(input(), 8)
    oct2 = int(input(), 8)
    
    sum = oct1 + oct2
    print(oct(sum)[2:]) # 숫자의 각 인덱스 중 2부터 (0o)44