# collections设置栈或者队列
# import collections
# collections.deque双端列表，头部插入与删除的时间复杂度为O(1)
# popleft,appendleft
# list(deque)还原变成list


# collections.Counter(xx)
# Counter()作为dict()的一个子类，可以求a['22'],a = collections.Counter()
# 输入列表，字符串，字典，将元素进行数量统计
# 计数后返回一个字典，键值为元素，值为元素个数
"""
str = "abcbcaccbbad"
li = ["a","b","c","a","b","b"]
print ("Counter(s):", Counter(str))
print ("Counter(li):", Counter(li))
Counter(s): Counter({'b': 4, 'c': 4, 'a': 3, 'd': 1})
Counter(li): Counter({'b': 3, 'a': 2, 'c': 1})
"""


# update
"""
d1 =Counter(str)
d1.update('123')
print(d1)
"""
# print增加了'123'，的字典


# 有序字典，defaultdict
"""
from collections import defaultdict
s=[('yellow',1),('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d=defaultdict(list)
for k, v in s:
    d[k].append(v)
a=sorted(d.items())
print(a)
"""
# 运行结果：
# [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]
# 可填list，set，dict等，结果会存为该格式
# 空结果返回是None
