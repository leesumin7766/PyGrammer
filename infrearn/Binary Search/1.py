# 정렬된 데이터에서 특정 값을 찾는 과정에서 절반씩 범위를 나눠가며 분할 정복 기법을 적용하는 알고리즘
def solution(target, nums) :
    left = 0
    right = len(nums) -1
    while left <= right :
        mid = (left + right) // 2
        if target == nums[mid] :
            return mid
        if target > nums[mid] :
            left = mid + 1
        else :
            right = mid - 1
    return -1

print(solution(8, [2, 5, 7, 8, 10, 15, 20, 24, 25, 30]))
print(solution(0, [-3,0,  2, 5, 8, 9, 12, 15]))
