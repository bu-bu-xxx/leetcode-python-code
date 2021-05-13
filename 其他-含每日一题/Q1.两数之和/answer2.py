# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 哈希表，把值作为索引，下标序号作为值
def twoSum(nums, target):
    hashtable = {}
    for i in range(len(nums)):
        val = nums[i]
        if target - val in hashtable:
            return [hashtable[target - val], i]
        else:
            hashtable[val] = i
    return []
