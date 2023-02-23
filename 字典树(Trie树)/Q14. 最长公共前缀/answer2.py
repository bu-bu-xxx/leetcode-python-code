# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 横向查找
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = min([len(word) for word in strs])
        for i in range(n):
            for word in strs:
                if word[i] != strs[0][i]:
                    return strs[0][0:i]
        return strs[0][0:n]
