# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做
# 调用自己写的Heap函数

from 堆.Heap.Heap import Heap


class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        Heap1 = Heap()
        nums = [-i for i in nums]
        Heap1.heapify(nums)
        for i in range(k - 1): Heap1.heappop(nums)
        return -Heap1.heappop(nums)


if __name__ == '__main__':
    try1 = Solution()

    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(try1.findKthLargest(nums, k))
