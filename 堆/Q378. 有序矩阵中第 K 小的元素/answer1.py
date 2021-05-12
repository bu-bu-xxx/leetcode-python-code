# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 直接排序
# 转成一维数组排序

class Solution:
    @staticmethod
    def kthSmallest(matrix, k):
        return sorted(sum(matrix, []))[k - 1]
