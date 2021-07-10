# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，阅读理解
# 二分搜索
import collections


class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mem = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mem[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        val_time = self.mem[key]
        if not val_time or timestamp < val_time[0][1]:
            return ""

        beg, end = 0, len(val_time)-1
        while beg != end:
            mid = round(beg + end)
            if val_time[mid][1] > timestamp:
                end = mid-1
            elif val_time[mid][1] <= timestamp:
                beg = mid
        return val_time[beg][0]


if __name__ == "__main__":
    try1 = TimeMap()
    try1.set("foo", "bar", 1)
    print(try1.get("foo", 1))
