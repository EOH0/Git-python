def is_leap_year(year):
    """윤년 판단 함수"""
    leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    return leap

def get_days_in_month(year, month):
    """주어진 연도와 월의 일 수 반환"""
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        months[1] = 29  # 윤년인 경우 2월은 29일
    return months[month - 1] # index니까 -1

def calculate_total_seconds(year, month, day, hour, minute, second):
    """연도, 월, 일, 시, 분, 초를 초로 변환하여 총 초 반환"""
    total_seconds = 0
    
    # 이전 연도까지의 총 일수
    for y in range(1, year):
        total_seconds += 365 * 24 * 3600 + is_leap_year(y) * 24 * 3600 # 윤년이면 하루 더 더함 (365 + 1)
    
    # 현재 연도의 월별 일 수 합산
    for m in range(1, month):
        total_seconds += get_days_in_month(year, m) * 24 * 3600
    
    # 현재 일, 시, 분, 초를 초로 변환하여 합산
    total_seconds += (day - 1) * 24 * 3600
    total_seconds += hour * 3600
    total_seconds += minute * 60
    total_seconds += second
    
    return total_seconds

def calculate_parking_fee(in_year, in_month, in_day, in_hour, in_min, in_sec, out_year, out_month, out_day, out_hour, out_min, out_sec):
    """주차 요금 계산"""
    in_total_seconds = calculate_total_seconds(in_year, in_month, in_day, in_hour, in_min, in_sec)
    out_total_seconds = calculate_total_seconds(out_year, out_month, out_day, out_hour, out_min, out_sec)

    total_parked_seconds = out_total_seconds - in_total_seconds

    # 10분(600초)당 요금 계산
    if total_parked_seconds <= 0:
        return 0  # 출차 시간이 입차 시간보다 이전이면 요금 0
    else:
        parking_fee = ((total_parked_seconds - 1) // 600 + 1) * 500  # 초 단위로 요금 계산 / 내림이니까 -1
        return parking_fee

if __name__ == "__main__":
    # 입차 시간 입력
    inYear = 2023
    inMonth = 12
    inDay = 27
    inHour = 10
    inMin = 20
    inSec = 30

    # 출차 시간 입력
    outYear = 2024
    outMonth = 3
    outDay = 7
    outHour = 19
    outMin = 0
    outSec = 5

    # 주차 요금 계산
    parking_fee = calculate_parking_fee(inYear, inMonth, inDay, inHour, inMin, inSec, outYear, outMonth, outDay, outHour, outMin, outSec
    )

    # 결과 출력
    print(f"주차 요금: {parking_fee}원")
