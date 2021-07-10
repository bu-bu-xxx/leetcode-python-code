# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，二分查找
# 求最高峰的开始和结束位置
import math
from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> tuple:
        def findLow(low, high):
            if low == high:
                return high
            mid = math.ceil((low + high) / 2)
            if arr[mid] > arr[mid - 1]:
                return findLow(mid, high)
            else:
                return findLow(low, mid - 1)

        def findHigh(low, high):
            if low == high:
                return high
            mid = (low + high) // 2
            if arr[mid] > arr[mid + 1]:
                return findLow(low, mid)
            else:
                return findLow(mid + 1, high)

        return findLow(0, len(arr)-1), findHigh(0, len(arr)-1)


if __name__ == "__main__":
    try1 = Solution()
    arr1 = [1, 2, 3, 3, 3, 2, 1]
    print(try1.peakIndexInMountainArray(arr1))
