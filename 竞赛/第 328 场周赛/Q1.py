# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 2535. 数组元素和与数字和的绝对差
from typing import List


class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum_all = 0
        sum_each = 0
        for num in nums:
            sum_all += num
            sum_each += sum([int(s) for s in list(str(num))])
        return abs(sum_all-sum_each)
