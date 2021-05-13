# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 动态规划，简化
# 用dp[i]存储加i次油能开到的最远距离
# 虽然复杂度一样，但是比自己写的好很多
# 还是有点复杂的，难写

class Solution:
    def minRefuelStops(self, target, startFuel, stations):
        dp = [startFuel] + [0] * len(stations)
        # 如果能到达这个站，则处理加油和不加油的值
        for i, (location, fuel) in enumerate(stations):
            # 到达i，前面加了i次油，这次是加了j次油
            for j in range(i, -1, -1):
                if dp[j] >= location:
                    dp[j + 1] = max(dp[j + 1], dp[j] + fuel)
        # 读出最少加油次数，能开到target
        for i, location in enumerate(dp):
            if location >= target:
                return i
        return -1


if __name__ == '__main__':
    try1 = Solution()

    target = 1000
    startFuel = 83
    stations = [[25, 27], [36, 187], [140, 186], [378, 6],
                [492, 202], [517, 89], [579, 234], [673, 86],
                [808, 53], [954, 49]]
    print(try1.minRefuelStops(target, startFuel, stations))
