dx = [-1, 0, 1, 0] # [상, 우, 하, 좌]
dy = [0, 1, 0, -1] # [상, 우, 하, 좌]
def DFS(x,y,board) :    # DFS 함수
    board[x][y] = 0     # 현재 위치가 (x,y)가 1일 경우 방문한 것으로 간주하고 0으로 바꿈
    for k in range(4) :     
        nx = x + dx[k]
        ny = y + dy[k]
        if nx >= 0 and nx < 5 and ny >= 0 and ny < 5 and board[nx][ny] == 1 :
            DFS(nx, ny, board)
    
def solution(board) :   # 5X5보드를 순회하면서 1을 찾으면 새로운 영역이므로 answer += 1
    answer = 0      
    for i in range(5) :
        for j in range(5) :
            if board[i][j] == 1 :
                answer += 1
                DFS(i, j, board)
    
    return answer

print(solution([[0,1,1,0,0], [0,1,1,0,0], [0,1,0,0,0], [0,0,0,1,0], [0,0,1,1,0]]))