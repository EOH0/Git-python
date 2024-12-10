import re

if __name__ == "__main__":
    fp = open("241205\\re_input.txt", "r")
    strs = fp.readlines()
    print(strs, len(strs))
    fp.close
    #date = re.compile('[0-9]{4}-[0-9]{2} [0-9]{2}:[0-9]{2}') # [0-9]{4}: 0~9까지 숫자 네자리
    date = re.compile('[0-9]+-[0-9]+-[0-9]+ [0-9]+:[0-9]+')
    ans = []
    for line in strs:
        if date.match(line):
            ans.append(line)
        else:
            print(line)
