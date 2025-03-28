def solution(m, n) :
    if m // n == 0:
        return m//n
    else :
        return m // n + 1
print(solution(1, 40))
print(solution(20, 4))
print(solution(4, 7))
print(solution(6, 20))