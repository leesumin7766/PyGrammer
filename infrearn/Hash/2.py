from collections import defaultdict, Counter
def solution(nums) :
    answer = -1
    nH = Counter(nums) #defaultdict(int)
    # for x in nums :
    #     nH[x] += 1
        
    for key in nH:
        if nH[key] == 1:
            answer = max(answer, key)
            
            
    return answer

print(solution([3,9,2,12,9,12,8,7,9,12]))