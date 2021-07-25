# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 官方答案，贪心算法
# 正向搜索
# 可以证明，每次都跨当前步数能到的最远距离
# 1.一定是最少步数到达终点
# 2.一定可以到达终点
# 每次走一步，想第二步最远能走到哪，即是最远距离
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        steps = 0
        position = 0
        while position < len(nums) - 1:
            if nums[position] + position >= len(nums) - 1:
                return steps + 1
            nex = [(position + i, position + i + nums[position + i]) for i in range(1, nums[position] + 1)]
            position = max(nex, key=lambda s: s[1])[0]
            steps += 1
