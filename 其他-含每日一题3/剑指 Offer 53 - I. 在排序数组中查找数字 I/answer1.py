# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，二分查找
import bisect
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return bisect.bisect_right(nums, target) - bisect.bisect_left(nums, target)
