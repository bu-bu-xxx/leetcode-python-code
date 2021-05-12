# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 堆法，自己写
# 取k个链表的头部值建最小堆
# 每次取出哪个堆的数就补回下一个值，因为最小值一定在这不多于k个值中
# 时间复杂度O(kn*log(k))，空间复杂度O(k)
from 链表.ListNode.ListNode import ListNode


class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None

        import heapq
        heap = []
        prev = ListNode()
        temp = prev
        # 构建小顶堆
        for l in lists:
            if l:
                heap.append(Heap(l))
        heapq.heapify(heap)
        # 出堆，入堆，排序
        while len(heap) > 0:
            if heap_next := heap[0].point.next:
                temp.next = heap[0].point
                temp = temp.next
                heapq.heapreplace(heap, Heap(heap_next))
            else:
                temp.next = heapq.heappop(heap).point
                temp = temp.next
        # 排序完
        return prev.next


class Heap:
    def __init__(self, node):
        self.node = node

    @property
    def point(self):
        return self.node

    def __lt__(self, other):
        return self.node.val < other.node.val

    # def __le__(self, other):
    #     return self.node.val <= other.node.val
    #
    # def __gt__(self, other):
    #     return self.node.val > other.node.val
    #
    # def __ge__(self, other):
    #     return self.node.val >= other.node.val


