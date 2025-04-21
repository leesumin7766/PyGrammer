from collections import Counter
def solution(S):
    sH = Counter(S)
    odd = 0
    for key in sH:
        if sH[key] % 2 == 1 :
            odd += 1
    
    return odd <= 1

        
    
print(solution("abacbaa"))