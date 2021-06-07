# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，儿童节特别题目，阅读题，简单
# 检测最少吃糖，和最多吃糖，之间，有没有要求的吃糖数量
from typing import List


class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        # 计算前i天的糖果总和
        for i in range(1, len(candiesCount)):
            candiesCount[i] += candiesCount[i - 1]
        candiesCount.append(0)
        answer = [False] * len(queries)
        for i, [Type, Day, Cap] in enumerate(queries):
            if (Day + 1) <= candiesCount[Type] and \
                    Cap * (Day + 1) >= candiesCount[Type - 1] + 1:
                answer[i] = True
        return answer


if __name__ == '__main__':
    try1 = Solution()
    candiesCount1 = [7, 4, 5, 3, 8]
    queries1 = [[0, 2, 2], [4, 2, 4], [2, 13, 1000000000]]
    print(try1.canEat(candiesCount1, queries1))
