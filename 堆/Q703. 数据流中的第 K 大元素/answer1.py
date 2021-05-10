# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 用堆解决，自己做
# 插入一个最小数，防止数组数量不够k个
# 取最大的k个数，用堆排序
# 判断最小的是否比新的数大，小则替换，大则忽略，然后读出最小数

import heapq


class KthLargest:

    def __init__(self, k: int, nums):
        nums.append(-10**7)
        nums = [-i for i in nums]
        heapq.heapify(nums)
        self.nums = []
        self.nums = [-heapq.heappop(nums) for i in range(k)]
        self.nums[-1::-1] = self.nums[:]

    def add(self, val: int) -> int:
        if self.nums[0] > val:
            return self.nums[0]
        else:
            heapq.heappush(self.nums, val)
            heapq.heappop(self.nums)
            return self.nums[0]
