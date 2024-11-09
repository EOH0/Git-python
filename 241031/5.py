if __name__ == "__main__":
# "{([]{}())}()[]" -> correct
# "{([]{}()}()[]" -> incorrect
    a = "{([]{}())}()[]"
    aL = []
    for ch in a:
        if len(aL) == a:
            aL.append(ch)
        else:
            if (aL[-1] == '{' and ch == '}') or (aL[-1] == '(' and ch == ')') or (aL[-1] == '[' and ch == ']'):
                aL.pop(-1)
            else:
                aL.append(ch)
    print(aL)

    if len(aL) == 0:
        print("correct")
    else :
        print("incorrect")