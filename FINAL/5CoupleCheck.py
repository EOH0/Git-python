if __name__ == "__main__":
    a = "{([]{}())}()[]" # -> correct
    # a = "{([]{}()}()[]" # -> incorrect
    aL = []
    for ch in a:
        if ch in "{[(":
            aL.append(ch)
        else:
            if len(aL) > 0 and ((aL[-1] == '{' and ch == '}') or 
                                (aL[-1] == '(' and ch == ')') or 
                                (aL[-1] == '[' and ch == ']')):
                aL.pop(-1)
            else:
                aL.append(ch)
        print(aL)
    if len(aL) == 0:
        print("correct")
    else:
        print("incorrect")