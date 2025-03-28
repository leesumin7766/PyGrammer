#ex
scores = [[75, 98,99],[84,98,78],[84,58,44],[74,59,89]] # 4명의 학생, 3과목

print(scores[0][2]) #1번째 학생의, 3번째 과목

for i in range(4) :
    for j in range(3) :
        print("[%d][%d] = %d" % (i, j, scores[i][j]))