# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 简单，自己做


class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        ch_dict = dict()
        for s in range(26):
            j = s % 5
            i = s // 5
            ch_dict[chr(ord('a') + s)] = (i, j)
        now_idx = (0, 0)
        res = ''
        for ch in target:
            nex_idx = ch_dict[ch]
            if ch != 'z':
                if (tmp := nex_idx[0] - now_idx[0]) >= 0:
                    res += 'D' * abs(tmp)
                else:
                    res += 'U' * abs(tmp)
                if (tmp := nex_idx[1] - now_idx[1]) >= 0:
                    res += 'R' * abs(tmp)
                else:
                    res += 'L' * abs(tmp)
            else:
                if (tmp := nex_idx[1] - now_idx[1]) >= 0:
                    res += 'R' * abs(tmp)
                else:
                    res += 'L' * abs(tmp)
                if (tmp := nex_idx[0] - now_idx[0]) >= 0:
                    res += 'D' * abs(tmp)
                else:
                    res += 'U' * abs(tmp)
            res += '!'
            now_idx = nex_idx

        return res
