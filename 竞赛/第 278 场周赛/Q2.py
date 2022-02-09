# encoding:utf-8
# @Author :ZQY


# 5981. 分组得分最高的所有下标
#
import collections
from typing import List


class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        record = collections.defaultdict(list)
        tmp = nums.count(1)
        for i in range(len(nums) + 1):
            if i != 0:
                if nums[i - 1] == 0:
                    tmp += 1
                else:
                    tmp -= 1
            record[tmp].append(i)
        return record[max(record.keys())]
