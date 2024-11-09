if __name__ == "__main__":
    a = [1, 6, 4, 3, 8, 8]
    sum = 0
    for i in range(len(a)):
        sum += a[i]
    avg = sum / len(a)

    print(avg)