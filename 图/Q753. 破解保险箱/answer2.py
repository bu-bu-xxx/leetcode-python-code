# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 官方答案，欧拉回路，Hierholzer算法
# 设置k^(n-1)个点，每一条出边代表新加一个点，有k条出边，k条入边
# 保证了有欧拉回路
# 共k^n条边，每条边构成均不同的密码
# 同样有k^n种密码，所以找到一条欧拉回路，即是一种密码
# 密码是ue1e2...e(end)，u为初始点
# Hierholzer算法：
# 所有出边出完了，才添加当前节点，最后得到倒序的点遍历顺序(点可能重复经过)


class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        if n == 1:
            return "".join([str(i) for i in range(k)])
        edges = set()
        road = []
        mod = 10 ** (n - 1)

        def dfs(node: int):
            for nex in range(k):
                if (edge := node * 10 + nex) not in edges:
                    edges.add(edge)
                    dfs(edge % mod)
            road.append(str(node % 10))

        dfs(0)
        return "0" * (n - 2) + "".join(road[::-1])
