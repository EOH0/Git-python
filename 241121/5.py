
if __name__ == "__main__":
    persons = [("강동원", 24), ("이정재", 31), ("정해인", 35), ("정우성", 30), ("변우석", 30)]

    # persons.sort(key = lambda x: x[0] + x[1], reverse=True)
    persons.sort(key = lambda x: x[1], reverse=True)

    print(persons)