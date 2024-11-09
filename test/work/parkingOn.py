def Isleap(year):
    return (year % 4 == 0) and (year % 400 == 0 or year % 100 != 0)

def DayMonth(year, month):
    Months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (Isleap(year)):
        Months[1] = 29
    return Months[month - 1]

def TotalSecond(Year, Month, Day, Hour, Min, Sec):
    Total = 0

    for i in range(1, Year):
        Total += 365 * 24 * 3600 + Isleap(i) * 24 * 3600
    for i in range(1, Month):
        Total += 24 * 3600 * DayMonth(Year, i)

    Total += (Day - 1) * 24 * 3600
    Total += Hour * 3600
    Total += Min * 60
    Total += Sec

    return Total

def calculPay(inYear, inMonth, inDay, inHour, inMin, inSec, outYear, outMonth, outDay, outHour, outMin, outSec):
    InSecond = TotalSecond(inYear, inMonth, inDay, inHour, inMin, inSec)
    OutSecond = TotalSecond(outYear, outMonth, outDay, outHour, outMin, outSec)

    result = OutSecond - InSecond

    if (result <= 0):
        pay = 0
    else:
        pay = ((result - 1) // 600 + 1) * 500
    
    return pay
    

if __name__ == "__main__":
    inYear = 2023
    inMonth = 12
    inDay = 27
    inHour = 10
    inMin = 20
    inSec = 30

    outYear = 2024
    outMonth = 3
    outDay = 7
    outHour = 19
    outMin = 0
    outSec = 5

    pay = calculPay(inYear, inMonth, inDay, inHour, inMin, inSec, outYear, outMonth, outDay, outHour, outMin, outSec)

    print(pay)
