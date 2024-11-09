if __name__ == "__main1__":
    f = open("C:\\Users\\seonh\\Documents\\Backup\\Coding\\Python\\241107\\1.txt", "w")

    for i in range(1, 11):
        f.write("%d\n"%i)
    
    f.close()
if __name__ == "__main2__":
    f = open("C:\\Users\\seonh\\Documents\\Backup\\Coding\\Python\\241107\\1.txt", "w", encoding="utf-8")

    for i in range(1, 11):
        f.write("%d번째 줄\n"%i)
    
    f.close()
if __name__ == "__main3__":
    f = open("C:\\Users\\seonh\\Documents\\Backup\\Coding\\Python\\241107\\1.txt", "r", encoding="utf-8")

    txts = f.read()

    print(txts)
if __name__ == "__main4__":
    f = open("C:\\Users\\seonh\\Documents\\Backup\\Coding\\Python\\241107\\1.txt", "r", encoding="utf-8")
    
    print(f.read(10),end="")
    print(f.read(10),end="")
    print(f.read(10))
    
    f.seek(0)

    print(f.read(10),end="")
    print(f.read(10),end="")
    print(f.read(10))

    f.seek(0)
    print(f.tell())
if __name__ == "__main5__":
    f = open("C:\\Users\\seonh\\Documents\\Backup\\Coding\\Python\\241107\\1.txt", "r", encoding="utf-8")
    for line in f:
        print(line,end="")
if __name__ == "__main__":
    f = open("C:\\Users\\seonh\\Documents\\Backup\\Coding\\Python\\241107\\1.txt", "r", encoding="utf-8")
    cnt = 0
    for line in f:
        if (line):
            cnt += 1
    print(cnt)
# 이미지 복사 프로그램
# 복사 프로그램 ->
    # open할때 "r", "w"는 안됨 <= 텍스트
    # "rb"로 열고, "wb"로 저장 binary 형태로 <= 파일을 통쨰로 읽음