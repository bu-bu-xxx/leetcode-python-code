# encoding:utf-8
# @Author :ZQY


# 5993. 将找到的值乘以2
import collections
from typing import List


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        count = collections.Counter()
        for num in nums:
            count[num] += 1
        while count[original] >=1:
            count[original]-=1
            original *= 2
        return original


if __name__=="__main__":
    try1 = Solution()
    nums = [5, 3, 6, 1, 12]
    original = 3
    print(try1.findFinalValue(nums, original))








