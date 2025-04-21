# 리스트나 튜플 같은 시퀀스를 반복할 때, 인덱스와 값을 동시에 가져오는 파이썬 내장 함수
arr = ['a', 'b', 'c']   # arr : 시퀀스
for index, value in enumerate(arr):
    # index: 요소의 인덱스 (0부터 시작)
    # value: 시퀀스 안의 실제 값
    print(index, value)