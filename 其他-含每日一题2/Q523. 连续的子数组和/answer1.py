# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，前缀和
# 太常规
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) <= 1:
            return False

        # 计算前缀和
        nums[0] %= k
        nums = [0] + nums

        # 遍历
        import collections
        pre = collections.Counter()

        for i in range(2, len(nums)):
            pre[nums[i-2]] += 1
            nums[i] = (nums[i - 1] + nums[i]) % k
            if nums[i] in pre:
                return True

        return False


if __name__ == "__main__":
    try1 = Solution()
    nums1 = [23, 0, 0]
    k1 = 6
    print(try1.checkSubarraySum(nums1, k1))
