# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做
# 普通做法，会超出时间限制，需要想一个时间复杂度更低的解法
# 要用到Trie前缀树(字典树)的知识，先放一下，等做到那，再来看这道题
from typing import List


class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        answer = []
        nums = sorted(nums)
        for x, m in queries:
            index = 0
            for n in range(len(nums)):
                if nums[n] <= m:
                    index += 1
            # 计算
            xor_sum = [x ^ k for k in nums[:index]]
            answer.append(max(xor_sum) if xor_sum else -1)

        return answer
