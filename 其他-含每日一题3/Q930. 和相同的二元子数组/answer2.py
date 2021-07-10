# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，前缀法改进
# ez
# 记录上一个1所在的位置
from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        tmp = -1
        pre = []
        for i, num in enumerate(nums):
            if num:
                pre.append(tmp)
                tmp = i
        pre.append(tmp)
        pre.append(len(nums))
        if goal > (len(pre) - 2):
            return 0

        res = 0
        if goal == 0:
            for i in range(1, len(pre)):
                res += (pre[i] - pre[i - 1] - 1) * (pre[i] - pre[i - 1]) // 2
            return res

        for j in range(goal, len(pre) - 1):
            i = j - goal + 1
            res += (pre[i] - pre[i - 1]) * (pre[j + 1] - pre[j])
        return res


if __name__ == "__main__":
    try1 = Solution()
    nums1 = [1, 0, 1, 0, 1]
    goal1 = 2
    print(try1.numSubarraysWithSum(nums1, goal1))
