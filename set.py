s1 = set([1, 2, 3])
s2 = set([3, 4, 5, 6])
print(list(s1))
print(s1 & s2) # 교집합 $
print(s1 | s2) # 합집합 |
print(s1 - s2) # 차집합 -
print(list(s1 - s2))     # 리스트형태
print(" ".join(map(str, s1 - s2)))      # 1 2