# 재귀함수 : 자기 자신을 호출하는 함수
# DFS : 깊이 우선 탐색

def DFS(n) :
    if n == 0 :
        return
    else :
        print(n, end = ' ')
        DFS(n-1)
DFS(5)

def DFS(n) :
    if n == 0 :
        return
    else :
        DFS(n-1)
        print(n, end = ' ')
DFS(5)