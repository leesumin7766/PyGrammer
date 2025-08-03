# 글로벌 함수 : 함수 안에서는 지역 변수로 표현되지만, global을 쓰면 전역 변수로 변환

x = 10
def change() :
    global x
    x = 20

change()
print(x)