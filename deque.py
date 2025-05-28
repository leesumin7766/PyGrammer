# deque vs queue.Queue  deque는 알고리즘 문제에 적합한 빠르고 간단한 자료구조
# append(), appendleft(), pop(), popleft()
from collections import deque
N_deque = deque([1, 2, 3, 4, 5])
N_deque.pop()
print(N_deque)
N_deque.append()
print(N_deque)
N_deque.popleft()
print(N_deque)
N_deque.appendleft()
print(N_deque)
# 파이썬에서는 함수의 리턴값을 바로 다른 함수의 인자로 넘길 수 있습니다.

N_deque.append(N_deque.popleft()) # == : x = N_deque.popleft() ,N_deque.append(x) 
print(N_deque)