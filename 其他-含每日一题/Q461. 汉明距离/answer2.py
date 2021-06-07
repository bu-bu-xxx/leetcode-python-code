# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 官方答案，移位


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        s = x ^ y
        result = 0
        # 求s的1的数量
        while s != 0:
            result += s & 1
            s = s >> 1
        return result


if __name__ == '__main__':
    try1 = Solution()
    x1 = 1
    y1 = 4
    print(try1.hammingDistance(x1, y1))
