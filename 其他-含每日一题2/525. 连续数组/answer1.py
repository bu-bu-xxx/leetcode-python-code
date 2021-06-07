# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 前缀和
# 计算1的个数-0的个数
# 找到前缀相同的值，则记录max
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # 前缀和
        nums = [0]+nums
        for i in range(1,len(nums)):
            if nums[i] ==1:
                nums[i] = nums[i-1] +1
            else:
                nums[i] = nums[i-1]-1
        # 遍历
        max_len = 0
        pre_dict = {0:0}
        for i in range(1,len(nums)):
            if nums[i] in pre_dict:
                max_len = max(max_len, i-pre_dict[nums[i]])
            else:
                pre_dict[nums[i]] = i
        return max_len


if __name__ == "__main__":
    try1 = Solution()
    nums1 = [0, 1, 0]
    print(try1.findMaxLength(nums1))


