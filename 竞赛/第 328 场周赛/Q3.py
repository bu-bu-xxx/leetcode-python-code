# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 2537. 统计好子数组的数目
import collections
from typing import List


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        rec = collections.Counter()
        right = 0
        tag = False
        res = 0
        val = [0]

        rec[nums[0]] += 1
        for left in range(n):
            if tag:
                break
            if left > 0:
                rec[nums[left - 1]] -= 1
                val[0] -= rec[nums[left - 1]]
            while 1:
                if val[0] >= k:
                    res += n - right
                    break
                right += 1
                if right == n:
                    tag = True
                    break
                rec[nums[right]] += 1
                val[0] += rec[nums[right]] - 1
        return res


if __name__ == "__main__":
    try1 = Solution()
    nums = [1, 1, 1, 1, 1]
    k = 10
    print(try1.countGood(nums, k))
