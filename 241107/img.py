import random

if __name__ == "__main__":
    fp = open("C:\\Users\\seonh\\Documents\\Backup\\Coding\\Python\\입력 파일.txt", "r", encoding="utf-8")

    txts = fp.read()
    print(txts) # 원본
    print()
    txts = txts.lower()
    fp.close()
    etcs = [".", ",", "(", "0", "'s", "[", "]"]
    while True:
        len1 = len(txts)
        for item in etcs:
            txts = txts.replace(item, "")
        len2 = len(txts)
        if len1 == len2:
            break
    print(txts) # lower + 특수문자떼기
    print()
    tlist = txts.split()
    print(tlist) # 단어 자르기
    print()
    counts_dic = dict()
    maxLengths = []
    maxLengths.append(tlist[0])
    for word in tlist:
        if word in counts_dic:
            counts_dic[word] += 1
        else:
            counts_dic[word] = 1
        if len(word) > len(maxLengths[0]):
            maxLengths.clear()
            maxLengths.append(word)
        elif len(word) == len(maxLengths[0]):
            maxLengths.append(word)
    print(maxLengths) # 가장 긴 문자
    print()
    print(counts_dic) # 문자 빈도 수
    print()
    maxCounts = []
    maxCounts.append(tlist[0])
    for key in counts_dic:
        if counts_dic[key] > counts_dic[maxCounts[0]]:
            maxCounts.clear()
            maxCounts.append(key)
        elif counts_dic[key] == counts_dic[maxCounts[0]]:
            maxCounts.append(key)
    print(maxCounts) # 가장 많은 빈도 수를 가지는 문자
