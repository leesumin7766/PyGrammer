def solution(nums) :
    n = len(nums) 
    can_ent = int(n / 2)
    cnt = 1
    nums.sort()
    for i in range(1, n) :
        if nums[i] != nums[i-1] :
            cnt += 1
            
    print(cnt)
    print(can_ent)
    if can_ent > cnt :
        return cnt 
    else :
        return can_ent

print(solution([2, 1, 1, 3, 2, 3, 1, 2]))