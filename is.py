# is 판별 문법
a = ["1" , "and", "ABC"]
# isdigit : 문자열 객체가 정수로 되어 있는지 판별
for i in a :
    print(f"isdigit: {i.isdigit()}")

# islower : 모두 소문자인지 확인
for i in a :
    print(f"islower: {i.islower()}")
    
# isUpper : 모두 대문자인지 확인
for i in a :
    print(f"isupper: {i.isupper()}")

# isspace : 공백 확인
for i in a :
    print(f"isspace: {i.isspace()}")
