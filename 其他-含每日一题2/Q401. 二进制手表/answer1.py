# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，简单
import collections
from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        h = collections.defaultdict(list)
        h[0] += ['0']
        h[1] += ['1', '2', '4', '8']
        h[2] += ['3', '5', '9', '6', '10']
        h[3] += ['7', '11']

        num = [1, 2, 4, 8, 16, 32]
        m = collections.defaultdict(list)
        m[0].append("00")

        def add_m(v: int, inx: int):
            if 0 <= v <= 9:
                m[inx].append("0" + str(v))
            elif 10 <= v <= 59:
                m[inx].append(str(v))

        for i1 in range(len(num)):
            v1 = num[i1]
            add_m(v1, 1)
            for i2 in range(i1 + 1, len(num)):
                v2 = num[i2]
                add_m(v1 + v2, 2)
                for i3 in range(i2 + 1, len(num)):
                    v3 = num[i3]
                    add_m(v1 + v2 + v3, 3)
                    for i4 in range(i3 + 1, len(num)):
                        v4 = num[i4]
                        add_m(v1 + v2 + v3 + v4, 4)
                        for i5 in range(i4 + 1, len(num)):
                            v5 = num[i5]
                            add_m(v1 + v2 + v3 + v4 + v5, 5)

        res = []
        for i in range(turnedOn + 1):
            for hh in h[i]:
                for mm in m[turnedOn - i]:
                    res.append(hh + ":" + mm)

        return res


if __name__ == "__main__":
    try1 = Solution()
    turnedOn1 = 9
    print(try1.readBinaryWatch(turnedOn1))
