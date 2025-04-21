#   새로운 리스트를 간편하게
#   new_list = [변수 활용 for 변수 in 반복대상 if 조건]
my_list = [1,2,3,4,5]
new_list = [x for x in my_list if x > 3]

print(new_list)