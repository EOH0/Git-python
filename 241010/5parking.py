if __name__ == "__main__" :
    inDay = 0
    inHour = 10
    inMin = 20
    inSec = 30

    outDay = 0
    outHour =  19 #19
    outMin = 0 #0
    outSec = 5 #5

    intime = inDay * 86400 + inHour * 3600 + inMin * 60 + inSec
    outtime = outDay * 86400 + outHour * 3600 + outMin * 60 + outSec
    charge = int((outtime - intime - 1)/600)
    print((charge + 1) * 500)


if __name__ == "__main2__" :
    inHour = 10
    inMin = 20
    inSec = 30

    outHour = 19
    outMin = 0
    outSec = 5

    hour = outHour - inHour
    min = outMin - inMin
    sec = outSec - inSec

    total_mins = int((hour * 60) + min + (sec / 60))
    print(total_mins)

    pay = 0
    while(total_mins >= 10) :
        pay += 500
        total_mins -= 10
    pay += 500
    print(pay)