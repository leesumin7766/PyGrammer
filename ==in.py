# ==(비교 연산자) : 값이 같은지 비교하는 연산자
a = 5
b = 5
c = 10
print(a == b)  # True, a와 b는 같은 값입니다.
print(a == c)  # False, a와 c는 다른 값입니다.

# in(멤버십 연산자) : 값이 (리스트, 튜플, 문자열)등에 포함되는지 확인
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)  # True, 3은 my_list에 존재합니다.
print(6 in my_list)  # False, 6은 my_list에 존재하지 않습니다.

my_string = "hello"
print('h' in my_string)  # True, 'h'는 "hello"에 존재합니다.
print('z' in my_string)  # False, 'z'는 "hello"에 존재하지 않습니다.
