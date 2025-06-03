# bisect : 정렬된 리스트에서 이진 탐색을 수행
from bisect import bisect_left, bisect_right
import bisect
arr = [1, 2, 4, 4, 4, 7, 10]

print(bisect.bisect_left(arr, 4)) # 4가 들어갈 가장 왼쪽 인덱스, 이미 4가 있다면 가장 왼쪽 4의 위치
# 출력: 2
print(bisect.bisect_right(arr, 4)) # 4가 들어갈 가장 오른쪽 인덱스, 이미 4가 있다면 가장 오른쪽 4의 위치
# 출력: 5

# 즉, 4는 인덱스 2, 3, 4에 있으며 총 3개
count = bisect.bisect_right(arr, 4) - bisect.bisect_left(arr, 4)

print(count)  # 출력: 3

arr.insert(bisect_left(arr, 4),3)
print(arr)
arr.insert(bisect_right(arr, 4),5)
print(arr)