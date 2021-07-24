# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做
# O(n)时间复杂度解法
import collections
from typing import List


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        dict_num = collections.Counter()
        n = len(arr)
        for num in arr:
            if num <= n:
                dict_num[num] += 1

        ans = 0
        for i in range(1, n + 1):
            dict_num[i] += dict_num[i - 1]
            ans = max(ans, dict_num[i] - i)

        return n - ans


if __name__ == "__main__":
    try1 = Solution()
    arr1 = [2, 2, 1, 2, 1]
    print(try1.maximumElementAfterDecrementingAndRearranging(arr1))
