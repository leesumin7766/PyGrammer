sH = dict();
# sH = {}
sH = {'a':3, 'b':5, 'c':2}
for key in sH :
    print(key) # a , b, c

for key, val in sH.items() :
    print(key, val) #a 3, b 5, c 2

print(len(sH))
del sH['a'] # 삭제
print(sH)