def solution(n, moves) :
    x = y = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    dir = ['U', 'R', 'D', 'L']
    
    for c in moves:
        for k in range(4):
            if c == dir[k]:
                nx = x + dx[k]
                ny = y + dy[k]
        if nx < 0 or nx >= n or ny < 0 or ny >= n : # 격자 밖으로 벗어나면 continue
            continue
        
        x = nx
        y = ny
    return [x, y]

print(solution(5, 'RRRDDDUUUUUUL'))
    