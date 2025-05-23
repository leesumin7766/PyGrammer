#sort함수
# nums.sort() # 오름차순 정렬
# nums.sort(reverse = True) # 내림차순 정렬
#좌표 정렬하기
def solution(nums):
    nums.sort(key = lambda v : (v[0]))
    return nums
print(solution([[2,3],[1,4],[3,1],[1,2]]))

def solution(nums):
    nums.sort(key = lambda v : (-v[0]))
    return nums
print(solution([[2,3],[1,4],[3,1],[1,2]]))
