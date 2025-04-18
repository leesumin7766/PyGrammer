from collections import deque
# deque : double-ended queue 양방향 큐
def solution(nums, k) :
    answer = deque(nums)
    for i in range(k) :
        answer.append(answer.popleft()) # 맨 왼쪽의 요소를 꺼내고, 맨뒤로 붙인다.
    
    return list(answer)
print(solution([3, 7, 1, 5, 9, 2, 8], 3))