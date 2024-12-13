if __name__ == "__main__":
    a = [[7], 
         [3, 8], 
         [8, 1, 0], 
         [2, 7, 4, 4], 
         [4, 5, 2, 6, 5]]
    for i in range(len(a) - 2, -1, -1):
        for j in range(len(a[i])):
            a[i][j] += max(a[i + 1][j], a[i + 1][j + 1])
    print(a)