# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 官方答案，确定有限状态自动机
# 大概就是根据当前状态，和输入的字符，计算变迁函数，得到输出的状态
# 计算时，先输入初始状态，然后得到终态，判断是否是想得到的最终状态
# 另外中间如果有非法字符，也会False
# 备注：自己尝试写写


class Solution:
    def isNumber(self, s: str) -> bool:
        # 把字符转换成字符表的大类
        def inChange(ch: str) -> str:
            if ord('0') <= ord(ch) <= ord('9'):
                return "num"
            if ord(ch) == ord('e') or ord(ch) == ord('E'):
                return "eE"
            if ord(ch) == ord('.'):
                return "."
            if ord(ch) == ord('+') or ord(ch) == ord('-'):
                return "+-"
            return "False"

        # 变迁函数
        func = {"0初始": {"+-": "1正负", "num": "1数", ".": "1无数字小数点"},
                "1正负": {"num": "1数", ".": "1无数字小数点"},
                "1数": {"num": "1数", ".": "1有数字小数点", "eE": "2字母"},
                "1无数字小数点": {"num": "1小数"},
                "1有数字小数点": {"num": "1小数", "eE": "2字母"},
                "1小数": {"num": "1小数", "eE": "2字母"},
                "2字母": {"+-": "2正负", "num": "2整数"},
                "2正负": {"num": "2整数"},
                "2整数": {"num": "2整数"},
                }

        def delta(Type: str, In: str) -> str:
            if In in func[Type]:
                return func[Type][In]
            else:
                return "False"

        # 正式输入
        type1 = "0初始"
        for s1 in s:
            in1 = inChange(s1)
            if in1 == "False":
                return False
            type1 = delta(type1, in1)
            if type1 == "False":
                return False
        return type1 in ["1有数字小数点", "1小数", "1数", "2整数"]
