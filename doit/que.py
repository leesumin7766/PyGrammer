from collections import deque
# 큐 구현을 위한 deque 라이브러리 사용
queue = deque()
#선입선출
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(9)
queue.popleft()

print(queue)
queue.reverse()
print(queue)