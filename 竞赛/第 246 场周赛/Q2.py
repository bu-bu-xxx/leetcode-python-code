# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 5789. 你完成的完整对局数


class Solution:
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        beginHH = int(startTime[0:2])
        endHH = int(finishTime[0:2])
        beginMM = int(startTime[3:5])
        endMM = int(finishTime[3:5])
        if endHH < beginHH:
            endHH += 24
        if endHH == beginHH and endMM < beginMM:
            endHH += 24

        res = 0
        if beginMM == 0:
            res += 4
        elif 0 < beginMM <= 15:
            res += 3
        elif 15 < beginMM <= 30:
            res += 2
        elif 30 < beginMM <= 45:
            res += 1

        if 0 <= endMM <= 14:
            res += 0
        elif 15 <= endMM <= 29:
            res += 1
        elif 30 <= endMM <= 44:
            res += 2
        elif 45 <= endMM <= 59:
            res += 3

        res += (endHH - beginHH - 1) * 4
        return res
