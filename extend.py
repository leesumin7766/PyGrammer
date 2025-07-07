# extend : 리스트에 다른 **리스트**의 모든 요소를 풀어서 추가
# append와 다름
a = [1, 2, 3]
a.extend([4, 5])
print(f"extend: {a}")

b = [1, 2, 3]
b.append([4, 5])
print(f"append: {b}")