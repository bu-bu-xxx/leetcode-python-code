# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，深度优先搜索
# 已经搜索完的或者搜索中的点不用再搜索
# 只需要存neighbor就可以


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        if node is None:
            return None

        node_new = Node(node.val)
        search_copy = {node.val: node_new}

        def dfs(node_now, node_copy):
            for neighbor in node_now.neighbors:
                if neighbor.val not in search_copy:
                    new = Node(neighbor.val)
                    search_copy[new.val] = new
                    dfs(neighbor, new)
                tmp = search_copy[neighbor.val]
                node_copy.neighbors.append(tmp)

        dfs(node, node_new)
        return node_new
