def solution(weight, limit) :
    answer = 0
    weight.sort()
    sum = 0 
    for i in weight :
        sum += i
        if sum <= limit :
            answer += 1
        else :
            return answer 

print(solution([300, 100, 230, 120, 90, 150, 60], 700))
print(solution([50, 90, 70, 300, 200, 150, 180, 190], 1000))
print(solution([70, 90, 100, 80, 60, 75, 73, 85, 120, 110, 200], 800))
print(solution([50, 90, 100, 130, 140, 120, 130, 120, 150, 160, 140, 170], 1000))
print(solution([50, 90, 100, 130, 140, 120, 130, 120, 150, 160, 140, 170], 350))