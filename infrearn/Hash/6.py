from collections import defaultdict

def solution(nums, target) :
    # answer = []
    # n = len(nums)
    # for i in range(n-1) :
    #     for j in range(i +1,n) :
    #         if nums[i] + nums[j] == target :
    #             answer.append(nums[i])
    #             answer.append(nums[j])
    
    # if len(answer) > 0 :
    #     return sorted(answer)
    # else :
    #     return [0, 0]
    answer = [0]*2
    nH = defaultdict(int)
    for x in nums :
        y = target -x
        if y in nH :
           return sorted([x,y])
        nH[x] = 1
    return answer 
    
print(solution([7,3,2,13,9,15,8,11], 12))
print(solution([7,5,12,20], 15))