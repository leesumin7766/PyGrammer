# 재귀 호출 기본 예제 : 팩토리얼
def DFS(n) :
    if n == 1 :
        return 1
    else :
        return n * DFS(n-1)

print(DFS(6))