# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 评论答案，二分查找，上升数列
# 思路和心得：
# 1.求最长公共子序列
# 2.找出arr每个数字在target中的index
# index是从左往右的====上升的
# LCS --> LIS 问题（前提是target中的数字互不相同，无重复数字！！！！！！！）
# 3.求LIS
# dp超时了
#
# 只能用贪心二分
# 注意：辅助数组a中不一定是LIS
import bisect
from typing import List


class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        dic = dict()
        for i, x in enumerate(target):
            dic[x] = i

        nums = []
        for x in arr:
            if x in dic:
                nums.append(dic[x])

        if not nums:
            return len(target)

        # LCS --> LIS
        a = []
        for x in nums:
            i = bisect.bisect_left(a, x)
            if i == len(a):
                a.append(x)
            else:
                a[i] = x

        return len(target) - len(a)








