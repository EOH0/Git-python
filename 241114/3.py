if __name__ == "__main__":
    # l.index(val)
    # ord, ch X
    msg = "AbclgPizlIvlJmIujqbqwca"
    alp1 = "abcdefghijklmnopqrstuvwxyz"
    alp2 = "abcdefghijklmnopqrstuvwxyz"

    for n in range(25):
        alp2 = alp2[1:] + alp2[0]
        print(alp2)
        ans = ""
        for i in range(len(msg)):        
            idx = alp1.index(msg[i].lower())
            if (msg[i].isupper()):
                ans += alp2[idx].upper()
            else:
                ans += alp2[idx]
        print(ans)

    