# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 可以看出方法一比方法二空间复杂度低
# 方法一空间复杂度O(n,k*log(n))，方法二O(n*log(k))

# 方法一
# 用heapq包和heapify做
"""
class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        import heapq
        nums = [-i for i in nums]
        heapq.heapify(nums)
        for i in range(k - 1): heapq.heappop(nums)
        return -heapq.heappop(nums)
"""


# 方法二
# 用heappush和heappop做
# 设置k大小的堆，不断更新

class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        import heapq
        heap = []
        for num_var in nums:
            if len(heap) < k:
                heapq.heappush(heap, num_var)
            else:
                heapq.heappush(heap, num_var)
                heapq.heappop(heap)
        return heap[0]
