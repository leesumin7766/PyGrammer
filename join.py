# 문자열 리스트를 하나의 문자열로 합치는 역할
#"구분자".join(리스트)

words = ["안녕", "세상", "Python"]
result = " ".join(words)  # 띄어쓰기로 연결
print(result)  # "안녕 세상 Python"

numbers = ["1", "2", "3", "4"]
result = "".join(numbers)  # 빈 문자열을 사용하여 붙이기
print(result)  # "1234"