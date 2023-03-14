# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 2576. 求出最多标记下标
# 二分法，可以推出，若最多有2*k个数，那么选最左边k个和最右边k个一定满足
# 然后二分k
# https://leetcode.cn/problems/find-the-maximum-number-of-marked-indices/solution/er-fen-da-an-pythonjavacgo-by-endlessche-t9f5/
from typing import List


class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        right = len(nums) // 2 + 1
        n = len(nums)
        while left < right - 1:
            k = (left + right) // 2
            if all(2 * nums[i] <= nums[n - k + i] for i in range(k)):
                left = k
            else:
                right = k

        return left * 2


if __name__ == "__main__":
    try1 = Solution()
    nums = [42, 83, 48, 10, 24, 55, 9, 100, 10, 17, 17, 99, 51, 32, 16, 98, 99, 31, 28, 68, 71, 14, 64, 29, 15, 40]
    print(try1.maxNumOfMarkedIndices(nums))
