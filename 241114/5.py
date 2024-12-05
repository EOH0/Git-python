def rank_by_order(arr):
    # 결과를 저장할 리스트 초기화
    ans = [0] * len(arr)
    
    # (값, 인덱스) 형태로 저장하여 정렬할 준비
    temp = []
    for i in range(len(arr)):
        temp.append((arr[i], i))  # 값과 인덱스를 쌍으로 저장
    
    # 값을 기준으로 내림차순 정렬
    temp.sort(reverse=True)

    # 순위를 매겨 결과 리스트에 저장
    rank = 1
    for i in range(len(temp)):
        value, original_index = temp[i]
        
        # 이전 값과 같으면 같은 순위를 부여
        if i > 0 and value == temp[i - 1][0]:
            ans[original_index] = ans[temp[i - 1][1]]
        else:
            ans[original_index] = rank
        rank += 1

    return ans

# 예제 테스트
if __name__ == "__main__":
    l = [3, 76, 24]  # 예제 입력
    print(rank_by_order(l))  # [3, 1, 2] 출력
    l = [3, 76, 24, 24]
    print(rank_by_order(l))  # [4, 1, 2, 2] 출력
