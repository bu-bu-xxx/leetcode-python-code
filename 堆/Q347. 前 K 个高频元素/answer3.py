# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，快速排序法

# 先用词典弄出出现频率，item变成列表
# 快速排序，在low和high中间随机选pivot
# pivot前面的是大的数，后面是小的数
# 如果是第k个，则读出，否则递归
# 不用考虑第k个有多个数字频率相同的情况，因为题设，只有一组解

class Solution:
    def topKFrequent(self, nums, k):
        import collections, random
        dict_nums = collections.Counter(nums)
        list_nums = list(dict_nums.items())

        def topK(low, high):
            pivot = random.randint(low, high)
            base = list_nums[pivot][1]
            list_nums[pivot], list_nums[low] = list_nums[low], list_nums[pivot]
            i = low + 1
            for j in range(low + 1, high + 1):
                if list_nums[j][1] > base:
                    list_nums[j], list_nums[i] = list_nums[i], list_nums[j]
                    i += 1
            i -= 1
            list_nums[low], list_nums[i] = list_nums[i], list_nums[low]
            if i == k - 1:
                return [num[0] for num in list_nums[0:k]]
            elif i < k - 1:
                return topK(i + 1, high)
            else:
                return topK(low, i - 1)

        return topK(0, len(list_nums) - 1)
