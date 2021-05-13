# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，动态规划
# 计算到每个加油站加油次数，和最多的油量，以及终点
# 并选同样加油次数的最大油量，并且加油次数多的油量要多于次数少的，删除负数油量
# 如果其中有一次为空，则不能到达，返回-1

class Solution:
    def minRefuelStops(self, target, startFuel, stations):
        # 起点，加油点，终点，用字典存(加油次数:油量)
        import collections
        record = [collections.Counter() for i in range(len(stations) + 2)]
        # 每到一个点，计算加油和不加油的油量，选最大油量存入字典
        record[0][0] = startFuel
        stations.append([target, 0])
        for i in range(1, len(stations) + 1):
            useFuel = stations[i - 1][0] if i == 1 \
                else stations[i - 1][0] - stations[i - 2][0]
            addFuel = stations[i - 1][1]
            if not record[i - 1]:
                return -1
            # 计算不同次数的油量，负数淘汰
            for (times, fuel) in sorted(record[i - 1].items()):
                if (temp := fuel - useFuel) >= 0:
                    record[i][times] = max(temp, record[i][times])
                    record[i][times + 1] = temp + addFuel
            # 遍历一边字典，去除加油次数多，但是油更少的
            maxFuel = -1
            for (times, fuel) in sorted(record[i].items()):
                if fuel < maxFuel:
                    del record[i][times]
                else:
                    maxFuel = fuel
        # 返回最小加油次数
        if not record[-1]:
            return -1
        return min(record[-1].keys())


if __name__ == '__main__':
    try1 = Solution()

    target = 100
    startFuel = 10
    stations = [[10, 60], [20, 30], [30, 30], [60, 40]]
    print(try1.minRefuelStops(target, startFuel, stations))
