# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，阅读理解，双指针
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        chars.append('1')
        left = 0
        count = 1
        for right in range(len(chars) - 1):
            if chars[right] != chars[right + 1]:
                chars[left] = chars[right]
                left += 1
                if count != 1:
                    for s in str(count):
                        chars[left] = s
                        left += 1
                count = 1
            else:
                count += 1

        return left


if __name__ == "__main__":
    try1 = Solution()
    chars1 = ["a", "a", "b", "b", "c", "c", "c"]
    print(try1.compress(chars1))
