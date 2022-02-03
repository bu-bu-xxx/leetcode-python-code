# encoding:utf-8
# @Author :ZQY


# 自己做，easy


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        tmp = ""
        for idx,s in enumerate(word):
            tmp = s+tmp
            if ch == s:
                return tmp + word[idx+1:]
        return word







