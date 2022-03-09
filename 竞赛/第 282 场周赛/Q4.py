# encoding:utf-8
# @Author :ZQY


# 2188. 完成比赛的最少时间
from typing import List


class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        max_num = 10 ** 7
        min_time_laps = [0] + [max_num] * 15
        for fi, ri in tires:
            for x in range(1, 16):
                if (tmp := fi * (ri ** x - 1) // (ri - 1)) > max_num:
                    break
                min_time_laps[x] = min(min_time_laps[x], tmp)

        dp = [0] + [max_num ** 2] * numLaps
        for lap in range(1, numLaps + 1):
            for last_change in range(max(0, lap - 15), lap):
                dp[lap] = min(dp[lap], dp[last_change] + changeTime + min_time_laps[lap - last_change])

        return dp[-1] - changeTime


if __name__ == "__main__":
    try1 = Solution()
    tires = [[2, 3], [3, 4]]
    changeTime = 5
    numLaps = 4
    print(try1.minimumFinishTime(tires, changeTime, numLaps))
