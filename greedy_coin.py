# 가장 큰 코인부터 최대한 많이 사용
coins = [500, 100, 50, 10]
amount = 4720
count = 0

for coin in coins:
    count += amount // coin
    amount %= coin

print(count)