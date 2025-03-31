#재귀함수 == 자기 자신을 다시 호출하는 함수
#재귀함수 사용 시, 재귀 함수의 종료 조건을 반드시 명시
def recursive_function() :
    print('재귀 함수를 호출합니다')
    recursive_function()
    
recursive_function()