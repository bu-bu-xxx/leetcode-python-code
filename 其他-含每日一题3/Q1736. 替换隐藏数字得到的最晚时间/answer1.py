# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，阅读理解


class Solution:
    def maximumTime(self, time: str) -> str:
        res = ""
        if time[0] == "?" and time[1] == "?":
            res += "23"
        elif time[0] == "?" and "0" <= time[1] <= "3":
            res += "2" + time[1]
        elif time[0] == "?" and time[1] > "3":
            res += "1" + time[1]
        elif time[1] == "?" and time[0] == "2":
            res += time[0] + "3"
        elif time[1] == "?":
            res += time[0] + "9"
        else:
            res += time[0:2]

        res += ":"

        if time[3] == "?":
            res += "5"
        else:
            res += time[3]

        if time[4] == "?":
            res += "9"
        else:
            res += time[4]

        return res
