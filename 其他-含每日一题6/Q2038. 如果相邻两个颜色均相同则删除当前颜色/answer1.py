# encoding:utf-8
# @Author :ZQY


# 自己做，非常easy题
# 代码写的是真的丑
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        A_times = 0
        B_times = 0
        A_len, B_len = 0, 0

        pre = colors[0]
        if pre == 'A':
            A_len += 1
        else:
            B_len += 1
        if colors[-1] == 'A':
            colors += 'B'
        else:
            colors += 'A'

        for ch in colors[1:]:
            if pre == ch:
                if ch == 'A':
                    A_len += 1
                else:
                    B_len += 1
            else:
                if ch == 'B':
                    A_times += max(0, A_len - 2)
                    A_len = 0
                    B_len = 1
                else:
                    B_times += max(0, B_len - 2)
                    A_len = 1
                    B_len = 0
            pre = ch
        return A_times > B_times


if __name__ == "__main__":
    try1 = Solution()
    colors = "AAAABBBB"
    print(try1.winnerOfGame(colors))
