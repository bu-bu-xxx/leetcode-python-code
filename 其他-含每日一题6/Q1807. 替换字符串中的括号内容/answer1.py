# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 简单
from typing import List


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        mark = 0
        tmp_key = ''
        res = ''
        knowledge_dict = dict()
        for key, value in knowledge:
            knowledge_dict[key] = value
        for ch in s:
            if mark == 0:
                if ch == '(':
                    mark = 1
                else:
                    res += ch
            elif mark == 1:
                if ch == ')':
                    mark = 0
                    if tmp_key in knowledge_dict:
                        res += knowledge_dict[tmp_key]
                    else:
                        res += '?'
                    tmp_key = ''
                else:
                    tmp_key += ch

        return res
