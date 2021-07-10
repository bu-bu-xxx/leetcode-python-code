# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，阅读理解
import collections
from typing import List


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.all_man = collections.defaultdict(list)
        self.dead_man = set()
        self.kingName = kingName

    def birth(self, parentName: str, childName: str) -> None:
        self.all_man[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead_man.add(name)

    def getInheritanceOrder(self) -> List[str]:
        res = []

        # 前序遍历
        def dfs(father: str):
            if father not in self.dead_man:
                res.append(father)
            for son in self.all_man[father]:
                dfs(son)

        dfs(self.kingName)
        return res

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
