# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 官方答案
# 用二进制的算法做
from typing import List


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(30):
            # c是第一位是1的个数
            c = sum(((val >> i) & 1) for val in nums)
            ans += c * (n - c)
        return ans


if __name__ == '__main__':
    try1 = Solution()
    nums1 = [4, 14, 2]
    print(try1.totalHammingDistance(nums1))
