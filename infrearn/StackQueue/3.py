def solution(s) :
    stack = []
    
    for i in s :
        if len(stack) == 0 :
            stack.append(i)
        elif i == stack[-1] :
            stack.pop(-1)
        else :
            stack.append(i)
    
    return str("".join(stack))

print(solution("acbbcaa"))
print(solution("bacccaba"))
print(solution("aabaababbaa"))