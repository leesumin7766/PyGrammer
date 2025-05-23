def solution(s) :
    stack = []
    for i in s :
        if i == '#' :
            stack.pop()
        else :
            stack.append(i)
    
    return "".join(stack)
    

print(solution("abc##ec#ab"))
print(solution('kefd#ef##s##'))
print(solution('teac#cher##er'))