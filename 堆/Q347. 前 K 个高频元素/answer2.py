# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，堆
# 字典记录出现次数，先用前k个数构建小顶堆，遍历剩下的，大于堆顶频率弹出堆顶并入堆
# 自己写堆

class Solution:
    def topKFrequent(self, nums, k):
        import collections
        dict_nums = collections.Counter(nums)
        result = []
        for key, val in dict_nums.items():
            if len(result) >= k:
                if val > result[0][0]:
                    heapreplace(result, (val, key))
            else:
                heappush(result, (val, key))
        return [i[1] for i in result]


# 自己写小顶堆的heappush和heapreplace，元组的情况下
def heappush(heap, item):
    i = len(heap)
    heap.append(item)
    while i > 0:
        i_father = (i - 1) // 2
        if heap[i_father][0] > item[0]:
            heap[i_father], heap[i] = heap[i], heap[i_father]
        i = i_father


def heapreplace(heap, item):
    heap[0] = item
    i = 0
    while 2 * i + 1 < len(heap):
        i_left = heap[2 * i + 1][0]
        i_right = heap[2 * i + 2][0] if (2 * i + 2) < len(heap) else 10 ** 8
        i_next = 2 * i + 1 if i_left < i_right else 2 * i + 2
        if item[0] > heap[i_next][0]:
            heap[i], heap[i_next] = heap[i_next], heap[i]
            i = i_next
        else:
            break


# 调用heapq包的解法
"""
class Solution:
    def topKFrequent(self, nums, k):
        import collections
        import heapq
        dict_nums = collections.Counter(nums)
        result = []
        for key, val in dict_nums.items():
            if len(result) >= k:
                if val > result[0][0]:
                    heapq.heapreplace(result, (val, key))
            else:
                heapq.heappush(result, (val, key))
        return [i[1] for i in result]
"""
