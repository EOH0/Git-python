if __name__ == "__main__" :
    mins = 26
    secs = 40
    mySecs = mins * 60 + secs
    mySecsPerKm = mySecs / 4
    speed = 3600 / mySecsPerKm

    print(mySecs, mySecsPerKm, speed, "km/h")

if __name__ == "__main2__" :
    distan = 4

    hour = 0
    min = 26
    sec = 40

    total_hours = min / 60 + sec / 3600

    kmh = distan / total_hours

    print(f"속도: {kmh} km/h")