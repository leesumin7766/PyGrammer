# 튜플 값은 변경되지 않는다.
# 튜플은 () 괄호로 만든다
person = ("Alice", 25)
print(person)  # 출력: ('Alice', 25)

# 여러 개의 튜플을 리스트로 저장할 수 있다
people = [("Alice", 25), ("Bob", 30), ("Charlie", 22)]
print(people)  # 출력: [('Alice', 25), ('Bob', 30), ('Charlie', 22)]

print(person[0])        # 이름 출력: Alice
print(person[1])        # 나이 출력: 25
########### input()
N = int(input())
people = []

for _ in range(N):
    name, age = input().split()
    people.append((name, int(age)))

print(people)

# 예시 입력: 3
#            Alice 25
#            Bob 30
#            Charlie 22