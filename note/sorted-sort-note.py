# sorted
# sorted语法格式：  sorted(可迭代对象,key=函数名,reverse=False/True)
# 作用：从可迭代对象中，依次取出一个元素，该元素再按照key规定的排列依据排序。
# 可迭代对象：即可依次取值的对象，例如：集合，序列（列表，字符串，元组），字典等。
# key : 是列表排列的依据，一般可以自定义一个函数返回排序的依据，再把函数名绑定给key。
# reverse : 译为反转，reverse默认等于False，从小到大排序。等于True时，从大到小排序。
"""
不能用 d_order=sorted(d,key=lambda x:x[1],reverse=False)
要用 d_order=sorted(d.items(),key=lambda x:x[1],reverse=False)
"""


# sort
# 列表的L.sort()方法：  L.sort(key=函数名,reverse=False/True)
# L.sort()：会自动遍历列表中的元素，即依次取出一个元素。再以key绑定的函数为依据排序。
"""
L = list(dict_items([('a', 1), ('c', 3), ('b', 2)])
L.sort(key=lambda x:x[1],reverse=False)
"""