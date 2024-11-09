if __name__ == "__main__":
    dow = ["일", "월", "화", "수", "목", "금", "토", "일"]
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year = int(input("년도 입력: "))
    month = int(input("월 입력: "))
    day = int(input("일 입력: "))

    days = (year - 1) * 365 + sum(months[:month - 1]) + day

    if month <= 2:
        year = year - 1
    days += int(year / 4)
    days -= int(year / 100)
    days += int(year / 400)

    print(f"{year}년 {month}월 {day}일은 {dow[days%7]}요일 입니다") 