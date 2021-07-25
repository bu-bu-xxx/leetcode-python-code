# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 官方答案，正向，贪心算法
# 可证明官方方法是可行得通的
# 只需要找最远能到的点即可
# https://leetcode-cn.com/problems/jump-game-ii/solution/tiao-yue-you-xi-ii-by-leetcode-solution/
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        position = len(nums) - 1
        steps = 0
        while position != 0:
            for i in range(0, len(nums)):
                if nums[i] + i >= position:
                    position = i
                    steps += 1
                    break
        return steps
