from collections import deque
def solution(nums) :
    queue = deque(nums)
    while queue :
        for _ in range(2):
            if len(queue) >= 2 :
                queue.popleft()
        queue.append(queue.popleft())
        
        if len(queue) == 1:
            return queue[0]
    
    
            
    
print(solution([3,1,4,5,2,6,7]))    

print(solution([10, 8 ,3 ,1, 6,4,7,10]))    
