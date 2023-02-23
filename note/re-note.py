# 正则表达式
# https://www.runoob.com/python/python-reg-expressions.html
"""
import re
re.findall(r'xxxx',str)

*：0个或多个，+：1个或多个，？：0个或1个

re.findall(r'[A-Z]+|[a-z]+','HaHH')
[('H',''),('','a'),('HH','')]
"""

# 找括号\( and \)

# 无括号返回list，list里面是str
# 有括号返回list，list里面是tuple，tuple里面是str
# 有括号则返回括号的内容，不返回括号外的内容
# 括号外面有个大括号，先返回大括号，再返回小括号，按左到右顺序

# a| b	匹配a或b
# (re)	对正则表达式分组并记住匹配的文本
# 加不加括号都是优先|，(a)(b)|(c)优先级等价于((a)(b))|(c)，后者比前者多输出一个

"""
例子：
txt = 'aa11bb22cc33'
rst = re.findall(r'[a-z]+\d+',txt)
print(rst))
rst = re.findall(r'([a-z]+)(\d+)',txt)
print(rst))
rst = re.findall(r'(([a-z]+)(\d+))',txt)
print(rst))
运行结果：
result=['aa11', 'bb22', 'cc33']
result=[('aa', '第 327 场周赛'), ('bb', '22'), ('cc', '33')]
result=[('aa11', 'aa', '第 327 场周赛'), ('bb22', 'bb', '22'), ('cc33', 'cc', '33')]
"""





