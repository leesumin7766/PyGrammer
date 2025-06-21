#   시퀀스(리스트, 튜플, 문자열 등) 거꾸로 뒤집은 반복자를 반환
#   정렬이 아닌 스택 순서를 뒤집는 것 !!!!
for i in reversed(range(5)):  # 4, 3, 2, 1, 0
    print(i)

for c in reversed("abc"):     # c, b, a
    print(c)