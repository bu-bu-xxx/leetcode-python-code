# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# easy
import collections


class Solution:
    def digitCount(self, num: str) -> bool:
        count = collections.Counter(num)
        for i in range(len(num)):
            if int(num[i]) != count[str(i)]:
                return False
        return True
