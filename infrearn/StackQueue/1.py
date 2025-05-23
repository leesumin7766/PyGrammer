# 코딩테스트에서 괄호 문제 대부분 스택
def solution(s) :
    is_stack = []
    for i in s :
        if i == "(" :
            is_stack.append(i)
        else :
            if len(is_stack) == 0 :
                return "NO"
            is_stack.pop()
            
    if len(is_stack) == 0 :
        return "YES"
    elif len(is_stack) == 1 :
        return "NO"
    
    
    
print(solution("((()))()"))
print(solution("((()))("))
print(solution("()())"))