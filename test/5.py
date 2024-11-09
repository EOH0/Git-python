if __name__ == "__main__":
    arr = [ 3, 5 ,8 ,55 ,13, 62, 72 ]
    n = 15

    cnt = 0
    for i in range(0, len(arr)):
        if (n < arr[i]):
            cnt += 1
    print(cnt)