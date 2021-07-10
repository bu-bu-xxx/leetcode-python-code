# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，广度优先搜索
# 先搜索完所有没搜索到的点，然后补全neighbor
import collections


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        if node is None:
            return None

        search = dict()
        # 初始化队列
        queue = collections.deque([node])
        node_new = Node(node.val)
        search[node.val] = node_new

        while queue:
            node_now = queue.popleft()
            node_copy = search[node_now.val]
            for tmp in node_now.neighbors:
                if tmp.val not in search:
                    new = Node(tmp.val)
                    search[tmp.val] = new
                    queue.append(tmp)
                node_copy.neighbors.append(search[tmp.val])

        return node_new
