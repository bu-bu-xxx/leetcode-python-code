# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 6284. 使字符串总不同字符的数目相等
# 参考别人的分类讨论做法
import collections


class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        dict1 = collections.Counter(word1)
        dict2 = collections.Counter(word2)
        for x, num1 in dict1.items():
            for y, num2 in dict2.items():
                if x == y and len(dict1) == len(dict2):
                    return True
                if x != y and (len(dict1) - (dict1[x] == 1) + (dict1[y] == 0)) == \
                        (len(dict2) - (dict2[y] == 1) + (dict2[x] == 0)):
                    return True
        return False
