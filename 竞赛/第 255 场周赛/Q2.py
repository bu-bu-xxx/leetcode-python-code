# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 5851. 找出不同的二进制字符串
from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = ""
        for i in range(len(nums)):
            if nums[i][i] == '0':
                res += "1"
            else:
                res += "0"
        return res

if __name__ == "__main__":














