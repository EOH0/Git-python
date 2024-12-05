if __name__ == "__main__":
    a = ["It", "was", "nearing", "midnight", "and", "the", "Prime", "Minister", "was", "sitting", "alone", "in", "his", "office", "reading", "a", "long", "memo", "that", "was", "slipping", "through", "his", "brain", "without", "leaving", "the", "slightest", "trace", "of", "meaning", "behind"]
    a = sorted(a, key=lambda x: (-len(x), x.lower()))
    print(a)