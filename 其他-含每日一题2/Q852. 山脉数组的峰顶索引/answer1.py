# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，二分查找
# 找最大值
from typing import List

"""
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        def find(low, high):
            if low == high:
                return high
            mid = (low + high) // 2
            if arr[mid] > arr[mid + 1]:
                return find(low, mid)
            else:
                return find(mid + 1, high)

        return find(0, len(arr) - 1)
"""


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low, high = 0, len(arr) - 1
        while low < high:
            mid = (low + high) // 2
            if arr[mid] > arr[mid + 1]:
                high = mid
            else:
                low = mid + 1
        return high
