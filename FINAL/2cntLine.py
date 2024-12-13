def cntLine(file_name):
    file = open(file_name, 'r', encoding='utf-8')  # fopen과 유사하게 파일 열기
    lines = file.readlines()  # 파일의 모든 줄 읽기
    print(lines)
    file.close()  # 파일 닫기
    # 빈 줄을 제외한 줄 계산
    lst = []
    for line in lines:  # 각 줄을 순회
        if line != '\n':  # 빈 줄이 아닌 경우 (줄 바꿈 문자만 있는 경우 제외)
            lst.append(line)  # 리스트에 추가

    return len(lst)

# 실행 부분
if __name__ == "__main__":
    file_name = "241031\in.txt"  # 파일 이름
    result = cntLine(file_name)
    print(result)
