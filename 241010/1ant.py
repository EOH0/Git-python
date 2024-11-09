if __name__ == "__main__" :
    gener = 5
    gener_cnt = 0

    sold = 3
    sold_cnt = 0

    work = 1
    work_cnt = 0
    
    flag = 1
    target = int(input())
    origin = target
    while flag:
        if (target >= gener):
            gener_cnt += target / gener
            target = target % gener
        elif (sold <= target < gener) :
            sold_cnt += target / sold
            target = target % sold
        elif (work <= target):
            work_cnt += target / work
            target = target % work
        else:
            flag = 0
    print(f"{int(origin)} -> {int(gener_cnt)} / {int(sold_cnt)} / {int(work_cnt)}")

        