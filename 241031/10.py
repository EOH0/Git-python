def largest_square(matrix):
    # matrix의 크기
    m = len(matrix)
    n = len(matrix[0])
    
    # DP 테이블 초기화
    dp = []
    for _ in range(m):
        dp.append([0] * n)

    max_size = 0
    
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '1':  # 현재 위치가 1일 때
                if i == 0 or j == 0:  # 첫 번째 행이나 열은 정사각형 크기가 1
                    dp[i][j] = 1
                else:
                    # 점화식 적용
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                # 가장 큰 정사각형 크기 업데이트
                max_size = max(max_size, dp[i][j])

    for i in range(m) :
        for j in range(n):
            print(dp[i][j], end=" ")
        print()
                
    return max_size

if __name__ == "__main__":
    matrix = [
        "1111111111",
        "1111101111",
        "1111111111",
        "1111111111",
        "1011111111", 
        "1111111111",
        "1111111111",
        "1111111011",
        "1111111111",
        "1111111111"
    ]
    
    # 입력을 2D 리스트로 변환
    matrix = [list(row) for row in matrix]
    
    # 가장 큰 정사각형 크기 출력
    print(largest_square(matrix))  # 출력: 5
