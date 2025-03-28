a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num*3)
print(result)

result = [num * 3 for num in a if num % 2 == 0] #result 리스트 안에 num* 3, 2로 나누었을 때 2로 나누어지는 = 짝수만 담기
print(result)