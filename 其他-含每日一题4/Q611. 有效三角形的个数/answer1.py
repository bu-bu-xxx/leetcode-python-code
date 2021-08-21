# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，二分查找
import bisect
from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        res = 0
        for a in range(n):
            for b in range(a + 1, n):
                res += max(0, bisect.bisect_left(nums, nums[a] + nums[b]) - b - 1)

        return res


if __name__ == "__main__":
    try1 = Solution()
    nums1 = [2, 2, 3, 4]
    print(try1.triangleNumber(nums1))
