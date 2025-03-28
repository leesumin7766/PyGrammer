strings = [["원두커피", "라떼", "콜라"], ["우동", "국수","피자"] ]

for i in range(len(strings)) :  #   len(strings) 리스트 행의 개수 : 2
    for j in range(len(strings[i])) :#  len(strings[i]) 리스트 각 행의 길이 : strings[0] = 3, strings[1] =3 
        print(strings[i][j])