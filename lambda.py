# 함수를 정의할 때 이름 없이 사용할 수 있는 방법
# lambda 매개변수: 표현식
# lambda 인자 : 반환값
def add(x, y):
    return x + y

add_lambda = lambda x, y: x + y
print(add_lambda(3, 4))  # 출력: 7
# 리스트 정렬 시, key로 람다 사용
points = [(1, 2), (3, 1), (0, 0)]
points.sort(key=lambda x: x[1])
print(points)  # 출력: [(0, 0), (3, 1), (1, 2)]

# map: 각 요소에 함수 적용
nums = [1, 2, 3]
squared = list(map(lambda x: x**2, nums))  # [1, 4, 9]
print(squared)
# filter: 조건을 만족하는 요소만 추출
evens = list(filter(lambda x: x % 2 == 0, nums))  # [2]
print(evens)
