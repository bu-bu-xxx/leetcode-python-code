# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 堆，自己做
# 尽可能用一箱油到更远的地方
# 当油够时，把油站存入堆中
# 当油不够时，出堆，并加油
# 得出到终点最少的加油次数
# 当堆为空且到达不了时，返回-1

class Solution:
    def minRefuelStops(self, target, startFuel, stations):
        import heapq
        heap = []  # 大顶堆
        times = 0
        cap = startFuel  # 能开多远的能力
        stations.append([target, 0])
        # 到达每个加油站的情况
        for (location, fuel) in stations:
            # 油够
            if cap >= location:
                heapq.heappush(heap, -fuel)
            # 油不够，则加到没油加为止
            else:
                while cap < location and heap:
                    cap += -heapq.heappop(heap)
                    times += 1
                # 当油加完，还是不够
                if cap < location and not heap:
                    return -1
                # 油加完了，够了
                heapq.heappush(heap, -fuel)

        return times
