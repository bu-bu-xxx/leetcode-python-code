# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，ez贪心算法
import collections
from typing import List


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        pairs_dict = collections.defaultdict(list)
        res = collections.deque()
        for lt, rt in adjacentPairs:
            pairs_dict[lt].append(rt)
            pairs_dict[rt].append(lt)

        mid = adjacentPairs[0][0]
        res.append(mid)
        # 左边插入
        now = mid
        pre = 10 ** 8
        while 1:
            for k in pairs_dict[now]:
                if k != pre:
                    res.appendleft(k)
                    pre = now
                    now = k
                    break
            if len(pairs_dict[now]) == 1:
                break

        # 右边插入
        now = mid
        pre = res[-2] if len(res) >= 2 else 10 ** 8
        while 1:
            for k in pairs_dict[now]:
                if k != pre:
                    res.append(k)
                    pre = now
                    now = k
                    break
            if len(pairs_dict[now]) == 1:
                break

        return list(res)


if __name__ == "__main__":
    try1 = Solution()
    adjacentPairs1 = [[2, 1], [3, 4], [3, 2]]
    print(try1.restoreArray(adjacentPairs1))
