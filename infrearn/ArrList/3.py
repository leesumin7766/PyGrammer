def solution(num) :
    answer = 0
    cnt = 0
    for x in num :
        if x == 1 :
            cnt += 1
        else :
            answer = max(answer, cnt) # 기존 ㅇanswer와 cnt 비교하여 큰 값으로 변경
            cnt = 0
    answer = max(answer, cnt) # 0으로 끝나지 않고 배열이 끝날 경우를 대비       
            
    return answer
print(solution([1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1]))