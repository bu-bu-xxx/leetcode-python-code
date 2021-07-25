# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 官方答案，排序，数学
# 和answer1一样的方法，排序不同
from typing import List


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

        for i in range(len(nums)):
            max_inx = i
            for j in range(i + 1, len(nums)):
                if cmp(nums[max_inx], nums[j]) == -1:
                    max_inx = j
            nums[i], nums[max_inx] = nums[max_inx], nums[i]

        res = ''.join(nums)
        if res[0] == "0":
            return "0"
        return res


if __name__ == "__main__":
    try1 = Solution()
    nums1 = [3, 30, 34, 5, 9]
    print(try1.largestNumber(nums1))
