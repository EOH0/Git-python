if __name__ == "__main__" :
    inDay = 0
    inHour = 10
    inMin = 20
    inSec = 30

    outDay = 0
    outHour =  10 #19
    outMin = 30 #0
    outSec = 30 #5

    intime = inDay * 86400 + inHour * 3600 + inMin * 60 + inSec
    outtime = outHour * 3600 + outMin * 60 + outSec
    charge = int((outtime - intime - 1)/600)
    print((charge + 1) * 500)
