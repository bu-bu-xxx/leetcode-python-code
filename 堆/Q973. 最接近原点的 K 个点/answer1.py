# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 用sorted排序

class Solution:
    def kClosest(self, points, k):
        from math import sqrt
        return sorted(points, key=lambda x: sqrt(x[0] ** 2 + x[1] ** 2))[0:k]
