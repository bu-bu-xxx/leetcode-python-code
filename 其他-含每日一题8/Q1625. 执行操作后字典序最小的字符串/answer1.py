# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 枚举
class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        rec = [s]
        res = s
        pre = s
        for i in range(len(s)):
            now = pre[-b:] + pre[:-b]
            if now != s:
                rec.append(now)
                res = min(res, now)
                pre = now
            else:
                break

        if b % 2 == 0:
            for s_pre in rec:
                for i in range(10):
                    s_new = ""
                    for idx in range(len(s_pre)):
                        if idx % 2 == 1:
                            s_new += str((int(s_pre[idx]) + a) % 10)
                        else:
                            s_new += s_pre[idx]
                    res = min(res, s_pre)
                    s_pre = s_new
        else:
            for s_pre in rec:
                for i in range(10):
                    s_new = ""
                    for idx in range(len(s_pre)):
                        if idx % 2 == 1:
                            s_new += str((int(s_pre[idx]) + a) % 10)
                        else:
                            s_new += s_pre[idx]
                    res = min(res, s_pre)
                    s_pre = s_new
                    for j in range(10):
                        s_new = ""
                        for idx in range(len(s_pre)):
                            if idx % 2 == 0:
                                s_new += str((int(s_pre[idx]) + a) % 10)
                            else:
                                s_new += s_pre[idx]
                        res = min(res, s_pre)
                        s_pre = s_new

        return res


if __name__ == "__main__":
    try1 = Solution()
    s = "5525"
    a = 9
    b = 2
    print(try1.findLexSmallestString(s, a, b))
