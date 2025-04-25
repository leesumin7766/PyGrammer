def solution(nums) :
    answer = 0
    n = len(nums)
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    
    for i in range(n) :
        for j in range(n) :
            flag = True # 현재 i행j열은 웅덩이가 맞다로 가정
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if nx >= 0 and nx < n and ny >= 0 and ny < n and nums[i][j] >= nums[nx][ny] :
                    flag = False
                    break
            
            if flag == True:
                answer += 1
    return answer

print(solution([[10,20,50,30,20], [20,30,50,70,90], [10,15,25,80,35],[25,35,40,55,40],[80,25,10,65,110]]))