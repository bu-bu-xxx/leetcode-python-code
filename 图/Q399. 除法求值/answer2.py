# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 官方答案，加权并查集
# 并查集分查询和合并两部分，特点是一边查询一边修改
# 查询就是查找根节点，会压缩路径为1，更新权重
# 合并就是先查找根，把不同树的根连在一起，包括合并树和新建边
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # 节点的父节点
        father = dict()
        # 节点到父节点的权值
        weight = dict()

        # 添加点
        def add(node):
            father[node] = None
            weight[node] = 1

        # 查询，要修改权值
        def find(node):
            if father[node] == None:
                return node
            tmp = father[node]
            father[node] = find(father[node])
            weight[node] *= weight[tmp]
            return father[node]

        # 合并，只合并不同根的
        def merge(a, b, val):
            a_root, b_root = find(a), find(b)
            if a_root != b_root:
                father[a_root] = b_root
                weight[a_root] = weight[b] / weight[a] * val

        # 预处理
        for [a, b], val in zip(equations, values):
            if a not in father:
                add(a)
            if b not in father:
                add(b)
            merge(a, b, val)

        # 回答问题
        res = []
        for [a, b] in queries:
            if a not in father or b not in father:
                res.append(-1)
                continue
            else:
                a_root, b_root = find(a), find(b)
                if a_root == b_root:
                    res.append(weight[a] / weight[b])
                else:
                    res.append(-1)
        return res
