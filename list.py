odd = [1,2,3,4,5]
a = [1, 2, 3, ['a', 'b', 'c']] # ['a', 'b', 'c']가 하나의 인덱스
print(type(odd))
print(odd[0])
print(odd[0]+ odd[3])
print(a[3])
print(a[3][-1]) # 이중 리스트 : a의 3번째 인덱스의 -1번째 = c
print(len(a)) # 리스트 길이
print(len(a[3])) # a의 4번째 리스트의 리스트 길이['a', b', 'c']
del odd[1] #2번째 인덱스 삭제
print(odd)
del a[2:] #3번째 부터 삭제
print(a)