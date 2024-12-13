if __name__ == "__main__":
    persons = [("강동원", 24), ("이정재", 31), ("정해인", 35), ("정우성", 30), ("변우석", 30)]

    # persons.sort(key = lambda x: x[0]) # 이름순
    persons.sort(key = lambda x: (x[1], x[0])) # 나이순으로 하는데 나이가 같으면 이름순

    print(persons)