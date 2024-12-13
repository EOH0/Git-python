def binary_search(arr, target):
    """
    이진 탐색 알고리즘
    :param arr: 정렬된 리스트
    :param target: 찾고자 하는 값
    :return: target 값의 인덱스 (찾을 수 없는 경우 -1 반환)
    """
    left, right = 0, len(arr) - 1  # 탐색 범위 초기화

    while left <= right:
        mid = (left + right) // 2  # 중간 인덱스 계산
        if arr[mid] == target:
            return mid  # 값을 찾으면 해당 인덱스 반환
        elif arr[mid] < target:
            left = mid + 1  # 탐색 범위를 오른쪽으로 좁힘
        else:
            right = mid - 1  # 탐색 범위를 왼쪽으로 좁힘

    return -1  # 값을 찾을 수 없는 경우 -1 반환

# 테스트
arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7
result = binary_search(arr, target)
if result != -1:
    print(f"값 {target}은(는) 인덱스 {result}에 있습니다.")
else:
    print(f"값 {target}을(를) 찾을 수 없습니다.")
