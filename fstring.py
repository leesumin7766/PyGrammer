# f-string은 Python 3.6부터 도입된 문자열 포매팅 방식, 문자열만 사용 가능
# 가독성 높은 문자열 출력을 가능, formatted string literals

# 문자열 앞에 f" 문자열 안에서 {변수 or 표현식}"
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")

x = 10
y = 5
print(f"x + y = {x + y}")

# 소수점 출력
answer = 123.456789
print(f"{answer:.1f}")
