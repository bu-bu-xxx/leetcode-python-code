# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 2574. 左右元素和的差值
from typing import List


class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        answer = []
        left = 0
        right = sum(nums)-nums[0]
        answer.append(abs(right))
        for i in range(1, len(nums)):
            left += nums[i - 1]
            right -= nums[i]
            answer.append(abs(left - right))
        return answer
