import re

if __name__ == "__main__":
    # 파일을 읽어들임
    with open("FINAL\\dirlist.txt", "r") as fp:
        files = fp.readlines()

    # 출력용 파일 리스트 확인
    print(files)

    # 날짜 형식을 찾기 위한 정규식 패턴
    date = re.compile(r'[0-9]{4}-[0-9]{2}-[0-9]{2}')

    print("===================================")
    
    # 파일 리스트에서 조건에 맞는 파일을 출력
    for file in files:
        file = file.strip()  # 줄바꿈 문자 제거

        # 날짜 형식이 맞고, "<DIR>"이 포함되지 않은 파일만 출력
        if date.match(file[:10]) and "<DIR>" not in file:
            print(f"{file}, file name: {file[39:]}")
