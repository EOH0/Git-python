if __name__ == "__main__":
    a = "rermgorpsam"
    b = [[2, 3], [0, 7], [5, 9], [6, 10]]
    for (i, j) in b:
        print(i, j)
        a = a[:i] + a[i:j+1][::-1] + a[j+1:]
        print(a)