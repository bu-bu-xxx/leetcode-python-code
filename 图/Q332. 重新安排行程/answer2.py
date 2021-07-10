# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 官方答案，Hierholzer 算法
# Hierholzer 算法用于在连通图中寻找欧拉路径，其流程如下：
# 1.从起点出发，进行深度优先搜索。
# 2.每次沿着某条边从某个顶点移动到另外一个顶点的时候，都需要删除这条边。
# 3.如果没有可移动的路径，则将所在节点加入到栈中，并返回。
# 4.最后倒序输出，得到欧拉回路或者欧拉路径
# 备注：本题前提条件，必须存在欧拉回路或者欧拉路径
import collections
import heapq
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(curr: str):
            while vec[curr]:
                tmp = heapq.heappop(vec[curr])
                dfs(tmp)
            stack.append(curr)

        vec = collections.defaultdict(list)
        for depart, arrive in tickets:
            vec[depart].append(arrive)
        for key in vec:
            heapq.heapify(vec[key])

        stack = list()
        dfs("JFK")
        return stack[::-1]


if __name__ == "__main__":
    try1 = Solution()
    tickets1 = [["A", "B"], ["JFK", "A"], ["B", "JFK"], ["A", "C"],
                ["C", "ZZZ"], ["ZZZ", "A"]]
    print(try1.findItinerary(tickets1))
