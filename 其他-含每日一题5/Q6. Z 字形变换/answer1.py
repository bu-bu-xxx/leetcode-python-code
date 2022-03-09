# encoding:utf-8
# @Author :ZQY


# 自己做，简单
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        row = [''] * numRows
        for idx, ch in enumerate(s):
            tmp = idx % (numRows * 2 - 2)
            if tmp < numRows:
                row[tmp] += ch
            else:
                row[numRows * 2 - 2 - tmp] += ch
        return ''.join(row)
