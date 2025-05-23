def solution(nums):
    stack = []
    answer = 0
    for i in nums :
        if len(stack) > 1 and i == 1 :
            if stack[-2] == 1 and stack[-1] == 2 and nums[i] ==1 :
                stack.pop(i-2) 
                stack.pop(i-1)
                answer += 1
            else :
                stack.append(i)
        else :
            stack.append(i)
    
    return answer

print(solution([1, 1, 1, 2, 1, 1, 2, 1, 2, 1]))
print(solution([1, 1, 1, 1,1,2,1,2]))
print(solution([1, 1, 1, 1,1,1,1]))