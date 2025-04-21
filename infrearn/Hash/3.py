from collections import Counter
def solution(nums) :
    answer = 100000000
    nH = Counter(nums)
    for key in nH:
        if nH[key] == key:
            answer = min(answer, key)
    return -1 if answer == 100000000 else answer

print(solution([1,2,3,1,3,3,2,4]))