# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，分类，赋值
# 遍历所有等式，存数值和属于的并查集编号
# 做题时，如果在一个并查集则计算，否则返回-1
# 备注：和加权并查集一个思路步骤，所以一样的复杂度
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        classify = dict()
        index = 0
        # 分类，name=[val,index]
        for i in range(len(values)):
            [A, B] = equations[i]
            val = values[i]
            if A in classify and B in classify:
                tmp = classify[A][1]
                w = classify[B][0]/classify[A][0]*val
                for key in classify.keys():
                    if classify[key][1] == tmp:
                        classify[key][0] *= w
                        classify[key][1] = classify[B][1]
            elif A in classify:
                classify[B] = [classify[A][0] / val, classify[A][1]]
            elif B in classify:
                classify[A] = [classify[B][0] * val, classify[B][1]]
            else:
                index += 1
                classify[B] = [1, index]
                classify[A] = [val, index]
        # 搜索
        res = []
        for [A, B] in queries:
            if A in classify and B in classify and \
                    classify[A][1] == classify[B][1]:
                res.append(classify[A][0] / classify[B][0])
            else:
                res.append(-1)
        return res
