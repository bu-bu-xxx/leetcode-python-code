# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 官方答案，排序，数学
# 定义a*b = ab>=ba
# 1.可证明*具有传递性，即a*b and b*c => a*c
# 2.可证明，对于一个最优序列，不存在a1，a2两个数，一前一后，但是a2*a1
# 因为，若a2*a1，且a1ba2>=a2ba1，则a1*b*a2，a1*a2，矛盾
from typing import List
import functools


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]

        def cmp(a, b):
            if a + b > b + a:
                return 1
            elif a + b < b + a:
                return -1
            else:
                return 0

        # 用了重载大于小于等于
        sorted_nums = sorted(nums, key=functools.cmp_to_key(cmp), reverse=True)
        res = ''.join(sorted_nums)
        if res[0] == "0":
            return "0"
        return res


if __name__ == "__main__":
    try1 = Solution()
    nums1 = [3, 30, 34, 5, 9]
    nums2 = [0, 0]
    print(try1.largestNumber(nums2))
