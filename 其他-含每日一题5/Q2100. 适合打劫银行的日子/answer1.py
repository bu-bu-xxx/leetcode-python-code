# encoding:utf-8
# @Author :ZQY


# 自己做，简单
from typing import List


class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        decrease_day = [0] * n
        increase_day = [0] * n
        for i in range(1, n):
            if security[i - 1] >= security[i]:
                decrease_day[i] = decrease_day[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if security[i + 1] >= security[i]:
                increase_day[i] = increase_day[i + 1] + 1

        res = []
        for i in range(n):
            if decrease_day[i] >= time and increase_day[i] >= time:
                res.append(i)

        return res


if __name__ == "__main__":
    try1 = Solution()
    security = [5, 3, 3, 3, 5, 6, 2]
    time = 2
    print(try1.goodDaysToRobBank(security, time))
