def solution(box, limit) :
    answer = 0
    box.sort(key = lambda v : -v[1])
    print(box)
    
    for i in box :
        cnt = min(limit, i[0])
        answer += (cnt * i[1])
        limit -= cnt
        if limit == 0:
            break
        
    return answer

print(solution([[2, 20], [2, 10], [3, 15], [2, 30]], 5))