# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 5788. 字符串中的最大奇数


class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[0:i + 1]
        return ""


if __name__ == "__main__":
    try1 = Solution()
    num1 = "52"
    print(try1.largestOddNumber(num1))
