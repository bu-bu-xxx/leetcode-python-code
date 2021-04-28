# 堆heapq模块
# 只支持最小堆，最大堆需要用相反数

# 模块heapq中一些重要的函数：
"""
heap = []:创建一个空堆
item = heap[0]:返回最小元素，但是不pop
heappush(heap, x):将x压入堆中
item = heappop(heap):从堆中弹出最小的元素
heapify(heap):把列表变成堆
item = heapreplace(heap, x):弹出最小的元素，并将x压入堆中
"""
import collections
print(collections.deque.__doc__)