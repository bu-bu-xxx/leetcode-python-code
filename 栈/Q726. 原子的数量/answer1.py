# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 递归法，自己做失败，错误程序，应该先把元素符号数字括号分装以后再递归的
# 一个括号一个递归
# 输入：当前括号的数量
# 接着计算括号内的数量
# 输出当前括号乘括号右标的总数量
# 先给整个加个大括号，右标为1
# dict_all里面名字是元素符号加第几层

class Solution:

    def countOfAtoms(self, formula: str) -> str:
        dict_all = {'now':0}
        formula = '(' + formula + ')' + '1'
        end = len(formula)
        now = 0

        def dfs(i, row, end):  # 循环到到第i个字符，第row层括号
            temp_word = ''
            temp_num = ''

            def count():
                # 结算上一个元素数量
                if temp_word != '':
                    if temp_word + str(row) in dict_all:
                        dict_all[temp_word + str(row)] += int(temp_num) if temp_num else 1
                    else:
                        dict_all[temp_word + str(row)] = int(temp_num) if temp_num else 1

            while i < end and formula[i] != ')':
                if formula[i] == '(':
                    # 先结算
                    count()
                    dfs(i + 1, row + 1, end)
                    i = dict_all['now']

                # 大写字母
                elif ord(formula[i]) >= ord('A') and ord(formula[i]) <= ord('Z'):
                    count()
                    temp_num = ''
                    temp_word = formula[i]

                # 小写字母
                elif ord(formula[i]) >= ord('a') and ord(formula[i]) <= ord('z'):
                    temp_word += formula[i]

                # 数字
                else:
                    temp_num += formula[i]

                i += 1


            # 循环结束
            # 把最后一个元素加上
            # 把这一层数值加到下一层上
            # 乘上尾数，并i退后一格
            # row减一
            count()
            i += 1

            dict_all_temp = dict_all.copy()
            for key1 in dict_all_temp.keys():
                if key1[-1] == str(row):
                    name = key1[0:len(key1) - 1] + str(row - 1)
                    dict_all[name] = dict_all[name] + dict_all[key1] if name in dict_all else dict_all[key1]
                    # del dict_all[key1]
            temp = ''
            while i < end:
                try:
                    kt = int(formula[i])
                    temp += formula[i]
                    i += 1
                except:
                    temp = int(temp)
                    i += 1

            for key2 in dict_all.keys():
                if key2[-1] == str(row):
                    dict_all[key2] = dict_all[key2] * temp

            dict_all['now'] = i

        # 从formula第2个开始
        dfs(1, 1, end)
        dict_res = {}
        for key in dict_all:
            if key[-1] == '0':
                dict_res[key[0:len(key) - 1]] = dict_all[key]

        return dict_res


if __name__ == '__main__':
    try1 = Solution()

    formula = "K4(ON(SO3)2)2"
    print(try1.countOfAtoms(formula))
