if __name__ == "__main__":
    a = "dfjardstddetckdaccccdegk" # -> “attack”
    n = 4
    # a = "pfqallllabwaoclk" # -> “fallback”
    # n = 2

    ans = ""
    for i in range(n - 1, len(a), n):
        ans += a[i]
    
    print(ans)



    # i = n - 1
    # while(i < len(a)):
    #     ans += a[i]
    #     i += n