# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 6284. 使字符串总不同字符的数目相等
# 讨论26*26个字母组合即可
import collections


class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        dict1 = collections.Counter(word1)
        dict2 = collections.Counter(word2)
        count = lambda dict0: len([s for s in dict0.values() if s > 0])

        for x in dict1.keys():
            for y in dict2.keys():
                dict1_tmp = dict1.copy()
                dict2_tmp = dict2.copy()
                dict1_tmp[x] -= 1
                dict2_tmp[x] += 1
                dict1_tmp[y] += 1
                dict2_tmp[y] -= 1
                if count(dict1_tmp) == count(dict2_tmp):
                    return True
        return False
