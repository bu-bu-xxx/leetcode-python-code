# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# Q3
# 5778. 使二进制字符串字符交替的最少反转次数
from typing import List


class Solution:
    def minFlips(self, s: str) -> int:
        def one(s1):
            count1 = [0, 0, 0, 0]  # 奇0,1，偶0,1
            for i, t in enumerate(s1):
                if i % 2 == 0:
                    if t == '0':
                        count1[2] += 1
                    else:
                        count1[3] += 1
                else:
                    if t == '0':
                        count1[0] += 1
                    else:
                        count1[1] += 1
            return count1

        def two(s2, count2: List[int]):
            if s2[0] == '0':
                return s2[1:] + s[0], [count2[2] - 1, count2[3], count2[0] + 1, count2[1]]
            else:
                return s2[1:] + s[0], [count2[2], count2[3] - 1, count2[0], count2[1] + 1]

        if len(s) % 2 == 0:
            count = one(s)
            return min(count[0] + count[3], count[1] + count[2])
        else:
            count = one(s)
            res = min(count[0] + count[3], count[1] + count[2])
            for i in range(len(s)):
                s, count = two(s, count)
                res = min(res, count[0] + count[3], count[1] + count[2])
            return res


if __name__ == '__main__':
    try1 = Solution()
    s1 = "01001001101"
    print(try1.minFlips(s1))
