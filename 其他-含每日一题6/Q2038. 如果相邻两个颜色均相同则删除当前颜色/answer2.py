# encoding:utf-8
# @Author :ZQY


# 自己做，写个好看点的，一行代码
import re


class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        # A_times = sum([max(0, len(tmp) - 2) for tmp in re.findall(r'[A]+', colors)])
        # B_times = sum([max(0, len(tmp) - 2) for tmp in re.findall(r'[B]+', colors)])
        # return A_times > B_times
        return sum([max(0, len(tmp) - 2) for tmp in re.findall(r'[A]+', colors)]) \
               > sum([max(0, len(tmp) - 2) for tmp in re.findall(r'[B]+', colors)])
