# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 简单
import collections


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        s_dict = collections.Counter(s)
        target_dict = collections.Counter(target)
        return min([s_dict[key] // target_dict[key] for key in target_dict.keys()])
