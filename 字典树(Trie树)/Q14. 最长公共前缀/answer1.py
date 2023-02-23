# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 普通查找
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = strs[0]
        for word in strs:
            pref = pref[0:len(word)]
            for i in range(len(pref)):
                if pref[i] != word[i]:
                    pref = pref[0:i]
                    break
            if pref == "":
                return ""

        return pref
