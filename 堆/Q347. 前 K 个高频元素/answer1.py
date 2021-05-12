# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，堆
# 字典记录出现次数，用堆排序出现次数，找出前k个
# 用heapify，再heappop前k个

class Solution:
    def topKFrequent(self, nums, k):
        # 字典记录出现频率
        import collections
        dict_nums = collections.Counter()
        for i in nums:
            dict_nums[i] += 1
        # 堆排序
        list_nums = list(dict_nums.values())
        list_nums = [-i for i in list_nums]
        import heapq
        heapq.heapify(list_nums)
        for i in range(k - 1):
            heapq.heappop(list_nums)
        nums_k = -list_nums[0]  # 第k高的出现频率
        # 找出频率大于nums_k的前k个词(前k个词不用这个条件，题目有假设答案唯一)
        result = []
        for key, value in dict_nums.items():
            if value >= nums_k:
                result.append(key)
        return result
