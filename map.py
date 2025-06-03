# map(함수, 반복 가능한 객체)의 각 요소에 함수를 적용해서 새로운 map 객체를 만듦
nums = ['1', '2', '3']
int_nums = list(map(int, nums))
print(int_nums)