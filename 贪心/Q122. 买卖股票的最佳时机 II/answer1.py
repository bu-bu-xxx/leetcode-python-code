# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，ez
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        now = prices[0]
        res = 0
        for price in prices[1:]:
            if price > now:
                res += price - now
            now = price
        return res


if __name__ == "__main__":
    try1 = Solution()
    prices1 = [7, 1, 5, 3, 6, 4]
    print(try1.maxProfit(prices1))
