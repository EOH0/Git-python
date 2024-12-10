if __name__ == "__main__":
    # numbers = [1, 2, 3, 4, 6, 7, 8]
    numbers = [5, 8, 4, 6, 7, 9]
    sum = 0
    for i in range(1, 10):
        if i not in numbers:
            sum += i
    print(sum)