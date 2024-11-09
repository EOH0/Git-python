if __name__ == "__main__":
    s = "abcdefghijklmnopqrstuvwxyz"

    arr = [0] * 26
    for i in range(0, 26):
        arr[ord(s[i]) - ord('a')] += 1
    print(arr)