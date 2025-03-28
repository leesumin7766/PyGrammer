#key, value값을 한 쌍으로 가지는 자료형
dic = {'name' : 'pey', 'phone' : '01-9999-9999', 'birth' : '24.05.05'}
print(dic)
dic['sex'] = 'male' # 딕셔너리 추가 : key['sex']에 value'male' 추가
print(dic)
print(dic.keys()) # 딕셔너리 키 리스트
del dic['sex'] # 딕셔너리 삭제 : key값 'sex'
print(dic)