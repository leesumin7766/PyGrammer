# re 사용
import re
p = re.compile('[a-z]+')    #p 패턴
m = p.match("python")
n = p.match("3 python")
print(m)
print(n)
n = p.search("3 python")
print(n)
f = p.findall("life is too short")
print(f)