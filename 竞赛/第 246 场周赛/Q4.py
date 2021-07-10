# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 5790. 查询差绝对值的最小值
from typing import List


class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        arr = []
        cnt = [0] * 101
        arr.append(cnt[:])
        for n in nums:
            cnt[n] += 1
            arr.append(cnt[:])

        res = []
        for [l, r] in queries:
            now = [i for i in range(101) if arr[r + 1][i] > arr[l][i]]
            if len(now) <= 1:
                res.append(-1)
                continue
            k = 1000
            for a0, a1 in zip(now, now[1:]):
                k = min(k, a1 - a0)
            res.append(k)

        return res


if __name__ == "__main__":
    try1 = Solution()
    nums1 = [1, 3, 4, 8]
    queries1 = [[0, 1], [1, 2], [2, 3], [0, 3]]
    print(try1.minDifference(nums1, queries1))
