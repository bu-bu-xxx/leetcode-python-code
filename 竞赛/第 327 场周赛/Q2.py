# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 6285. 执行 K 次操作后的最大分数
import bisect
import heapq
import math
from typing import List


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-a for a in nums]
        heapq.heapify(nums)
        res = 0
        for _ in range(k):
            num = heapq.heappop(nums)
            heapq.heappush(nums, math.floor(num / 3))
            res += -num
        return res


if __name__ == "__main__":
    try1 = Solution()
    print(try1.maxKelements([1, 10, 3, 3, 3], 3))
