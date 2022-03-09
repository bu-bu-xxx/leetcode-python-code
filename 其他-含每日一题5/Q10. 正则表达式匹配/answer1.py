# encoding:utf-8
# @Author :ZQY


# 自己做，先用re
import re


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        tmp = re.findall(p, s)
        return len(tmp) >= 1 and len(tmp[0]) == len(s)


if __name__ == "__main__":
    try1 = Solution()
    s = 'aa'
    p = 'a*'
    print(try1.isMatch(s, p))
