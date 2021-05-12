# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 用堆排序
# heapq默认用元组的第一个值排序，用指针标志points，节省空间
# 前k个可以用heapify时间更短，但是我不用，诶，就是玩

class Solution:
    @staticmethod
    def kClosest(points, k):
        from math import sqrt
        import heapq
        count = lambda s: -sqrt(s[0] ** 2 + s[1] ** 2)
        heap = []
        for i, point in enumerate(points):
            if len(heap) >= k:
                temp = count(point)
                if heap[0][0] < temp:
                    heapq.heapreplace(heap, (temp, i))
            else:
                heapq.heappush(heap, (count(point), i))
        return [points[i[1]] for i in heap]
