N [::]
#문자열[start:end:step] 처음(기본 1) : 해당인덱스 -1 : 몇글자씩(기본 1)

#ex
N = "baekjoon"
print(N[::-1]) #"noojkeab" 처음부터 끝까지 -1씩 ===> -1부터 끝까지 -1씩

#ex
text = "abcdef"
print(text[::-1])  # "fedcba"
print(text[::2])   # "ace"  (0, 2, 4번째 문자 가져옴)
print(text[::-2])  # "fdb"  (뒤에서 2칸씩 이동)


 