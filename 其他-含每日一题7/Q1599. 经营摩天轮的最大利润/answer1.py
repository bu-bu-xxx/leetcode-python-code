# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 自己做，阅读理解
from typing import List


class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if 4 * boardingCost - runningCost <= 0:
            return -1

        res = 0
        max_val = 0
        cur_val = 0
        cus = 0
        for i in range(len(customers)):
            cus = cus + customers[i]
            if cus > 4:
                cus -= 4
                cur_val += 4 * boardingCost - runningCost
            else:
                cur_val += cus * boardingCost - runningCost
                cus = 0
            if cur_val > max_val:
                max_val = cur_val
                res = i + 1

        if cus > 0:
            i = len(customers) + (cus // 4)
            cur_val += (4 * boardingCost - runningCost) * (cus // 4)
            cus = cus % 4
            if cur_val > max_val:
                res = i
                max_val = cur_val
        if cus > 0 and (cus * boardingCost - runningCost) > 0:
            res += 1
        return res if res > 0 else -1
