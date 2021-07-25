# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 5811. 用三种不同颜色为网格涂色


# class Solution:
#     def colorTheGrid(self, m: int, n: int) -> int:
#         mod = 10**9 + 7
#         # [三种颜色数量]
#         state = [[[0, 0, 0]] * n for _ in range(m)]
#         st1 = lambda s1, s2: [(s1[1] + s1[2]) * (s2[1] + s2[2]),
#                               (s1[0] + s1[2]) * (s2[0] + s2[2]),
#                               (s1[1] + s1[0]) * (s2[1] + s2[0])]
#         st2 = lambda s: [s[1] + s[2], s[0] + s[2], s[1] + s[0]]
#
#         for i in range(m):
#             for j in range(n):
#                 if i - 1 >= 0 and j - 1 >= 0:
#                     state[i][j] = st1(state[i - 1][j], state[i][j - 1])
#                 elif i - 1 >= 0:
#                     state[i][j] = st2(state[i - 1][j])
#                 elif j - 1 >= 0:
#                     state[i][j] = st2(state[i][j - 1])
#                 else:
#                     state[i][j] = [1, 1, 1]
#
#         return sum(state[-1][-1])%mod
import collections


class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        mod = 10 ** 9 + 7
        st_set = set()
        state = collections.defaultdict(list)

        def dfs():
            if len(stack) == m:
                st_set.add(tuple(stack))
                return
            for nex in {1, 2, 3} - {stack[-1]}:
                stack.append(nex)
                dfs()
                stack.pop()

        stack = [1]
        dfs()
        stack = [2]
        dfs()
        stack = [3]
        dfs()
        for i, st in enumerate(st_set):
            for j, st1 in enumerate(st_set):
                tag = True
                for k in range(m):
                    if st[k] == st1[k]:
                        tag = False
                        break
                if tag is True:
                    state[i].append(j)

        dp = [1] * len(st_set)
        for _ in range(n - 1):
            dp_nex = [0] * len(st_set)
            for i in range(len(dp)):
                for j in state[i]:
                    dp_nex[j] += dp[i]
            dp = dp_nex

        return sum(dp) % mod


if __name__ == "__main__":
    try1 = Solution()
    m1 = 5
    n1 = 5
    print(try1.colorTheGrid(m1, n1))
