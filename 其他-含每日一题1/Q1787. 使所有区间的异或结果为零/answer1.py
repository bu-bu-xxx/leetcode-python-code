# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 官方答案和自己思考结合，迭代，动态规划
# 把nums分成k组，间隔为k分组，要使每组数相同
# 分两种情况，一种是允许选择的数x与n[i]中的不同，一种是x in n[i]
# 第一种情况，n[i]中最大重复数最少的i，自由选取，其余选取count(i,x)最大值
# 第二种情况，迭代函数为min_f(i,mask^x)=f(i-1,mask)+len(n[i])-count(i,x)
# 其中，f(i,mask)指和为mask的前i组n的最小修改元素数
# count(i,x)指n[i]中x的数量
# 每次迭代，选取x in n[i]更新f(i,mask)，mask重复的选取最小值
from typing import List


class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        # 设置n
        import collections
        count = [collections.Counter() for _ in range(k)]
        count_len = [0 for _ in range(k)]
        for i in range(len(nums)):
            count[i % k][nums[i]] += 1
            count_len[i % k] += 1

        # 第一种情况
        count = sorted(count, key=lambda s: max(s.values()), reverse=True)
        # 这个result只是一个上限，真正的值是两种情况的min
        result1 = len(nums) - sum([max(s.values()) \
                                   for s in count[0:len(count) - 1]])

        # 第二种情况
        f = collections.Counter()
        f[0] = 0  # 初始化，哨兵
        for i in range(k):
            temp = collections.Counter()
            for mask in f.keys():
                for x in count[i].keys():
                    val = mask ^ x
                    temp[val] = min(temp[val], f[mask] - count[i][x] + count_len[i]) \
                        if temp[val] else f[mask] - count[i][x] + count_len[i]
            f = temp

        # 结果
        if 0 not in f:
            return result1
        result2 = f[0]
        return min(result2, result1)


if __name__ == '__main__':
    try1 = Solution()
    nums1 = [1, 2, 4, 1, 2, 5, 1, 2, 6]
    k1 = 3
    print(try1.minChanges(nums1, k1))
