# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 暴力算法
def twoSum(nums,target):
    n = len(nums) # nums长度
    for i in range(n):
        for j in range(i+1,n):
            if nums[i]+nums[j]==target:
                return [i,j]
    return []







