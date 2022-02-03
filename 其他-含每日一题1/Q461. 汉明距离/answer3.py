# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 官方答案，Brian Kernighan算法
# 进行x&(x-1)运算计算1的数量


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        s = x ^ y
        result = 0
        while s:
            s = s & (s - 1)
            result += 1
        return result


if __name__ == '__main__':
    try1 = Solution()
    x1 = 1
    y1 = 4
    print(try1.hammingDistance(x1, y1))

