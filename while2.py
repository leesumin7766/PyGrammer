coffee = 10
money = 10
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee =coffee -1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지")
        break