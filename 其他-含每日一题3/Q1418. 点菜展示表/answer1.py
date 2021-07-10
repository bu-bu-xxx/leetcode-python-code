# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，哈希表
from typing import List


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        show = dict()
        table_mark = set()
        for customer, table, food in orders:
            table = int(table)
            if food not in show:
                show[food] = [0] * 501
            show[food][table] += 1
            table_mark.add(table)

        res = [["Table"] + list(sorted(show.keys()))]
        table_mark = sorted(table_mark)
        for t in table_mark:
            res.append([str(t)] + [str(show[key][t]) for key in sorted(show.keys())])

        return res


if __name__ == "__main__":
    try1 = Solution()
    orders1 = [["David", "3", "Ceviche"], ["Corina", "10", "Beef Burrito"], ["David", "3", "Fried Chicken"],
               ["Carla", "5", "Water"], ["Carla", "5", "Ceviche"], ["Rous", "3", "Ceviche"]]
    print(try1.displayTable(orders1))
