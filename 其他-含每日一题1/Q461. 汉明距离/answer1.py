# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，一行
# 用函数包做


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        import re
        return len(re.findall(r'([1])', str(bin(x ^ y))))


if __name__ == '__main__':
    try1 = Solution()
    x1 = 1
    y1 = 4
    print(try1.hammingDistance(x1, y1))
