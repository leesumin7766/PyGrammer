from collections import Counter
from collections import deque
from collections import defaultdict
from collections import OrderedDict
from collections import namedtuple
#Counter
word = "mississippi"
counter = Counter(word)
print(counter)  # {'i': 4, 's': 4, 'p': 2, 'm': 1}
print(counter.most_common(2))  # [('i', 4), ('s', 4)]

#deque
dq = deque([1, 2, 3])
dq.append(4)  # 오른쪽 추가
dq.appendleft(0)  # 왼쪽 추가
print(dq)  # deque([0, 1, 2, 3, 4])
dq.pop()  # 오른쪽 제거
dq.popleft()  # 왼쪽 제거
print(dq)  # deque([1, 2, 3])

#defaultdict
dd = defaultdict(int)  # 기본값이 0
dd["apple"] += 1
print(dd)  # {'apple': 1}
dd_list = defaultdict(list)  # 기본값이 빈 리스트
dd_list["fruits"].append("apple")
print(dd_list)  # {'fruits': ['apple']}

#OrderedDict
od = OrderedDict()
od['apple'] = 3
od['banana'] = 2
od['cherry'] = 5
print(od)  # OrderedDict([('apple', 3), ('banana', 2), ('cherry', 5)])

#namedtuple
Point = namedtuple('Point', ['x', 'y'])  # x, y 필드가 있는 튜플 생성
p = Point(10, 20)
print(p.x, p.y)  # 10 20
print(p)  # Point(x=10, y=20)