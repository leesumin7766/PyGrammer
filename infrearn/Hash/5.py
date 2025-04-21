from collections import Counter
def solution(S):
    sH = Counter(S)
    odd = 0
    dee = 0
    for i in sH :
        if sH[i] % 2 == 1 :
            odd += 1
    if odd > 0 :
        return len(S) - odd + 1
    else :
        return len(S)
            

print(solution("abcbbbccaaeee"))
