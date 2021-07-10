# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，回溯算法
# 尝试每一种路径
import collections


class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        # 构造所有需要的密码
        all_set = collections.deque([""])
        for _ in range(n):
            for i in range(len(all_set)):
                tmp = all_set.popleft()
                all_set += [tmp + str(kk) for kk in range(k)]
        all_set = set(all_set)

        # 回溯搜索
        res = "0" * (n - 1)
        tag = False

        def dfs(now: str):
            nonlocal res, tag, all_set
            if len(all_set) == 0:
                tag = True
                return
            for nex in range(k):
                if (nex_str := now + str(nex)) in all_set:
                    all_set -= {nex_str}
                    res += str(nex)
                    dfs(nex_str[1:])
                    if tag:
                        return
                    all_set |= {nex_str}
                    res = res[:-1]

        dfs(res[:])
        return res
