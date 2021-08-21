# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 官方答案，递归分治
# [i,j]树结构中j为根节点
# 找到[i+1,m]均小于j，保证[m+1,j-1]大于j即可
from typing import List


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        flag = True

        def check(beg, end):
            nonlocal flag
            if beg >= end:
                return
            root = postorder[end]
            left = beg - 1
            for i in range(beg, end):
                if postorder[i] < root:
                    left += 1
                else:
                    break
            for i in range(left + 1, end):
                if postorder[i] < root:
                    flag = False
                    return
            check(beg, left)
            check(left + 1, end - 1)

        check(0, len(postorder) - 1)
        return flag
