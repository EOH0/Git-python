if __name__ == "__main__":
    l = [3, 76, 24, 24]
    bl = l[:]
    bl.sort(reverse=True)
    ans = []
    for i in range(len(l)):
        ans.append(bl.index(l[i]) + 1)
    print(ans)
    