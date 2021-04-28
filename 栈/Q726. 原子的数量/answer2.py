# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 正则表达式re.findall做

# (:开启下一层
# )num:乘上这一层，加到下一层，并删除这一层
# 按名字sorted排序

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        import re
        import collections
        parse = re.findall(r'([A-Z][a-z]*)([0-9]*)|(\()|(\))([0-9]*)', formula)
        stack = [collections.Counter()]  # 每一层元素数量
        for atom_name, atom_num, left, right, kuo_num in parse:
            if atom_name:
                stack[-1][atom_name] += int(atom_num) if atom_num else 1
            elif left:
                stack.append(collections.Counter())
            elif right:
                temp = stack.pop()
                times = int(kuo_num) if kuo_num else 1
                for key in temp.keys():
                    temp[key] *= times
                    stack[-1][key] += temp[key]

        res = ''
        # 按名字sorted排序
        for key in sorted(stack[-1].keys()):
            res += key
            res += str(stack[-1][key]) if stack[-1][key] > 1 else ''

        return res


if __name__ == '__main__':
    try1 = Solution()

    formula = "K4(ON(SO3)2)2"
    print(try1.countOfAtoms(formula))
