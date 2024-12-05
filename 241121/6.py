from itertools import combinations
from itertools import permutations
if __name__ == "__main__":
    a = [2,1,3,4,1]
    # b = list(combinations(a,2))
    b = list(permutations(a, 2))
    print(b)
    ans = []
    for item in b:
        temp = item[0] + item[1]
        if (temp not in ans):
            ans.append(temp)
    print(ans)
    ans.sort()
    print(ans)
