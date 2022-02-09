# encoding:utf-8
# @Author :ZQY


# 5995. 字符串分组
# 看了官方答案，虽然不难，但是也是值得思考
# 思路：
# 每个字符串用二进制表示，作为一个节点
# 搜索节点的所有相邻节点，然后用并查集，或bfs，或dfs搜索
# 每个点有最多196个相邻节点，时间复杂度为O(n*|nodes|)，|nodes|=196
import collections
from typing import List


"""并查集，居然超出时间限制
class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        n = len(words)
        nodes_dict = collections.Counter()

        # 生成二进制节点
        for word in words:
            key = 0
            for ch in word:
                key |= 1 << (ord(ch) - ord('a'))
            nodes_dict[key] += 1

        # 邻接点，并查集
        rec = dict()
        for key in nodes_dict.keys():
            rec[key] = key

        def search(node):
            if rec[node] == node:
                return node
            rec[node] = search(rec[node])
            return rec[node]

        def merge(node1, node2):
            rec[search(node1)] = search(node2)

        for key in nodes_dict.keys():
            # 找邻接点
            # 修改0->1
            for i in range(27):
                tmp = key
                if not (1 << i) & key and i != 26:
                    tmp = tmp | (1 << i)
                # 修改1->0
                for j in range(27):
                    if (1 << j) & key and j != 26:
                        tmp = tmp - (1 << j)
                    # 找到邻接点tmp
                    if tmp in nodes_dict:
                        merge(tmp, key)
                    if (1 << j) & key and j != 26:
                        tmp += 1 << j

        # 返回结果
        count = collections.Counter()
        for node in rec.keys():
            count[search(node)] += nodes_dict[node]
        res = [len(count), max(count.values())]
        return res
"""


class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        # 使用哈希映射统计每一个二进制表示出现的次数
        wordMasks = collections.Counter()
        for word in words:
            mask = 0
            for ch in word:
                mask |= (1 << (ord(ch) - ord("a")))
            wordMasks[mask] += 1

        # 辅助函数，用来得到 mask 的所有可能的相邻节点
        def get_adjacent(mask: int) -> List[int]:
            adj = list()
            # 将一个 0 变成 1，或将一个 1 变成 0
            for i in range(26):
                adj.append(mask ^ (1 << i))
            # 将一个 0 变成 1，且将一个 1 变成 0
            for i in range(26):
                if mask & (1 << i):
                    for j in range(26):
                        if not (mask & (1 << j)):
                            adj.append(mask ^ (1 << i) ^ (1 << j))
            return adj

        used = set()
        best = cnt = 0
        for mask, occ in wordMasks.items():
            if mask in used:
                continue

            # 从一个未搜索过的节点开始进行广度优先搜索，并求出对应连通分量的大小
            q = collections.deque([mask])
            used.add(mask)
            # total 记录联通分量的大小
            total = occ

            while q:
                u = q.popleft()
                for v in get_adjacent(u):
                    if v in wordMasks and v not in used:
                        q.append(v)
                        used.add(v)
                        total += wordMasks[v]

            best = max(best, total)
            cnt += 1

        return [cnt, best]



