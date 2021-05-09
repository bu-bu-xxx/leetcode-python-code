# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 堆：即是优先队列
# 堆的特点：
# 1.内部数据是有序的
# 2.可以弹出堆顶的元素，大顶堆就是弹出最大值，小顶堆就是弹出最小值
# 3.每次加入新元素或者弹出堆顶元素后，调整堆使之重新有序仅需要O(logn)的时间
# 4.支持在线算法
# 添加元素：
# 1.把新元素放在树末尾
# 2.逐层往上走到自己的位置
# 弹出堆顶元素：
# 1.把堆顶元素和堆末尾元素对调位置
# 2.删除堆末尾元素(即是堆顶元素)
# 3.逐层往下走到自己的位置


# 默认为小顶堆

class Heap:

    def __init__(self):
        self.heap = []

    @property
    def size(self):
        return len(self.heap)

    def _swap(self, a, b):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]

    def _up(self, index):
        # 向上遍历父节点，调整好位置
        while index > 0:
            father_index = (index - 1) // 2
            if self.heap[father_index] > self.heap[index]:
                self._swap(father_index, index)
            index = father_index

    def _down(self, index):
        # 向下遍历子节点，调整好位置
        # 一律向右子节点遍历
        while (index * 2 + 1) < self.size:
            left_index = index * 2 + 1
            right_index = index * 2 + 2 if (index * 2 + 2) < self.size else left_index
            min_index = right_index if self.heap[right_index] < self.heap[left_index] else left_index
            if self.heap[min_index] < self.heap[index]:
                self._swap(min_index, index)
            index = min_index

    def heappush(self, list, value):
        self.heap = list
        self.heap.append(value)
        self._up(self.size - 1)
        list = self.heap

    def heappop(self, list):
        self.heap = list
        self._swap(0, self.size - 1)
        val = self.heap.pop()
        self._down(0)
        list = self.heap
        return val

    def heaptop(self, list):
        self.heap = list
        return self.heap[0]

    def heapify(self, list):
        # 输入一个列表，然后格式化成堆
        self.heap = list
        row = 1
        if self.size == 1: return
        while 1:
            if 2 ** (row + 1) - 1 > self.size >= 2 ** row - 1:
                break
            row += 1
        for index in range(2 ** row - 2, -1, -1):
            self._down(index)
        list = self.heap



