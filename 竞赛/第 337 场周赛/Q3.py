# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 6352. 美丽子集的数目
import collections
from typing import List


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        rec_set = collections.defaultdict(set)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    rec_set[i].add(j)

        res = 0

        def dfs(idx, pre):
            nonlocal res
            res += 1
            for nex in range(idx + 1, len(nums)):
                if nex not in pre:
                    dfs(nex, pre | rec_set[nex])

        for i in range(len(nums)):
            dfs(i, rec_set[i])

        return res


if __name__ == "__main__":
    try1 = Solution()
    nums = [4, 2, 5, 9, 10, 3]
    k = 1
    print(try1.beautifulSubsets(nums, k))
