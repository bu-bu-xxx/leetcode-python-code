# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 分块+预处理，官方答案
# 每k个数分成一块，计算每个数在分块中前缀的最大值preMax(不含自己)，后缀的最大值sufMax(含自己)
# 对于窗口，开始点i的后缀最大值，和i+k的前缀最大值，的最大值，为所求

class Solution:
    def maxSlidingWindow(self, nums, k):
        # k=1的特殊情况
        if k == 1:
            return [nums[i] for i in range(0, len(nums) - k + 1)]

        n = len(nums)
        preMax = [0] * (n + 1)
        sufMax = [0] * (n - 1) + [nums[n - 1]]
        # 计算sufMax和preMax，sufMax的最后一个数是特殊情况
        for i in range(1, n + 1):
            preMax[i] = nums[i - 1] if i % k == 1 else max(nums[i - 1], preMax[i - 1])
        for i in range(n - 2, -1, -1):
            sufMax[i] = nums[i] if i % k == (k - 1) else max(nums[i], sufMax[i + 1])
        # 计算滑动窗口最大值
        # result = []
        # for i in range(0, n - k + 1):
        #     result.append(max(sufMax[i], preMax[i + k]))
        return [max(sufMax[i], preMax[i + k]) for i in range(0, n - k + 1)]
