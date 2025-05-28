def solution(k, nums):
    answer = 0
    n = len(nums)
    for i in range(k + 1):
        sumN = 0
        for j in range(i) :
            sumN += nums[j]
        for j in range(n - k + i, n) :
            sumN += nums[j]
        answer = max(answer, sumN)

    return answer

print(solution(4,[2, 3 ,7, 1, 2, 1, 5]))
print(solution(5,[1, 2, 3 ,5 ,6 ,7, 1, 3, 9]))