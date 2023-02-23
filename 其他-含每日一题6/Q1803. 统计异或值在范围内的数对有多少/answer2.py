# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 哈希表
import collections
from typing import List


class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        high_bit = 15
        nums_dict = [None] * high_bit
        for i in range(high_bit):
            nums_dict[i] = collections.Counter([num >> i for num in nums])

        def count(x: int, t: int):
            res = 0
            tmp = 0
            for i in range(high_bit - 1, -1, -1):
                x_bit = (x >> i) & 1
                t_bit = (t >> i) & 1
                if t_bit:
                    res += nums_dict[i][(tmp << 1) + (x_bit ^ 0)]
                    tmp = (tmp << 1) + (x_bit ^ 1)
                else:
                    tmp = (tmp << 1) + (x_bit ^ 0)
            res += nums_dict[0][tmp]
            return res

        res = 0
        for num in nums:
            res += count(num, high) - count(num, low - 1)
        return res // 2


if __name__ == "__main__":
    nums = [1, 4, 2, 7]
    low = 2
    high = 6
    try1 = Solution()
    print(try1.countPairs(nums, low, high))
