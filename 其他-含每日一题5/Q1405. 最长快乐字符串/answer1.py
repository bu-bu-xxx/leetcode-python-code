# encoding:utf-8
# @Author :ZQY


# 自己做，数学，贪心
# 真的完全是硬凑出来的代码


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ''
        record = dict()
        record['a'], record['b'], record['c'] = a, b, c
        # 当至少两个不为0
        while (a + b + c) != max(a, b, c):
            v1, v2, v3 = sorted([(a, 'a'), (b, 'b'), (c, 'c')])
            if (v3[0] // 2) > (v2[0] + v1[0]):
                res += v3[1] * 2
                res += v2[1]
                record[v3[1]] -= 2
                record[v2[1]] -= 1
            else:
                res += v3[1]
                res += v2[1]
                record[v3[1]] -= 1
                record[v2[1]] -= 1
            a, b, c = record['a'], record['b'], record['c']

        max_key = max(['a', 'b', 'c'], key=lambda s: record[s])
        if record[max_key] == 1:
            res += max_key
        elif record[max_key] >= 2:
            res += max_key * 2

        return res
