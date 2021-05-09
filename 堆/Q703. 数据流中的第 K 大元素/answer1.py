# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 用堆解决，自己做
# 每次都取k个，然后插入回去

import heapq


class KthLargest:

    def __init__(self, k: int, nums):
        if nums:
            nums = [-i for i in nums]
            heapq.heapify(nums)
            if len(self.nums) >= k:
                self.nums = [-heapq.heappop(nums) for i in range(k)]
            else:
                self.nums = [-heapq.heappop(nums) for i in range(k - 1)]
            self.nums[-1::-1] = self.nums[:]
        else:
            self.nums = nums
        self.k = k

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        if self.nums[0] >= val:
            return self.nums[0]
        else:
            heapq.heappush(self.nums, val)
            heapq.heappop(self.nums)
            return self.nums[0]
