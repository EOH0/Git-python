if __name__ == "__main__":
    arr2D = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    max = 0
    sum = []
    for i in range(len(arr2D)):
        insum = 0
        for j in range(len(arr2D[i])):
            insum += arr2D[i][j]
        sum.append(insum)
    for i in range(len(sum)):
        if max < sum[i]:
            max = sum[i]
    for i in range(len(sum)):
        print(sum[i])
    print("MAX:", max)