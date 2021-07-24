# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，二分查找
# 加油加油加油
import math
from typing import List


class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        nums3 = [abs(nums1[i] - nums2[i]) for i in range(n)]
        nums1 = sorted(nums1)
        mod = 10 ** 9 + 7

        def search(num, low, high):
            """
            :param num:搜索的数
            :return: 最小的绝对值差
            """
            if low == high:
                if low == -1:
                    return abs(nums1[0] - num)
                if low == n - 1:
                    return abs(nums1[-1] - num)
                else:
                    return min(abs(num - nums1[low]), abs(num - nums1[low + 1]))

            mid = math.ceil((low + high) / 2)
            if mid == -1:
                mid_val = float('-inf')
            elif mid == n:
                mid_val = float('inf')
            else:
                mid_val = nums1[mid]

            if mid_val == num:
                return 0
            elif mid_val < num:
                low = mid
            else:
                high = mid - 1
            return search(num, low, high)

        max_val = 0
        for i, num in enumerate(nums2):
            max_val = max(max_val, nums3[i] - search(num, -1, n))
        return (sum(nums3) - max_val) % mod


if __name__ == "__main__":
    try1 = Solution()
    nums11 = [2, 4, 6, 8, 10]
    nums22 = [2, 4, 6, 8, 10]
    print(try1.minAbsoluteSumDiff(nums11, nums22))
