import copy

if __name__ == "__main__":
    L = [[1, 2, 3], [1,2], [3,5], [5, 2, 2, 1, 5]]
    sum = 0
    max = 0
    numval = L[0][0]
    # for i in range(len(L)):
    #     for j in range(len(L[i])):
    #         sum += L[i][j]
    #         if (max < L[i][j]):
    #             max = L[i][j]
    for i in L:
        sum += sum(i)
        max = max(max, max(L))
    print(sum, max)