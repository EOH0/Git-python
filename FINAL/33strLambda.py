if __name__ == "__main__":
    a = ["It", "was", "nearing", "midnight", "and", "the", "Prime", "Minister", "was", "sitting", "alone", "in", "his", "office", "reading", "a", "long", "memo", "that", "was", "slipping", "through", "his", "brain", "without", "leaving", "the", "slightest", "trace", "of", "meaning", "behind"]
    
    # 길이가 긴 순으로 정렬하고, 길이가 같으면 사전순으로 정렬
    a_sorted = sorted(a, key=lambda x: (-len(x), x))
    
    print(a_sorted)
