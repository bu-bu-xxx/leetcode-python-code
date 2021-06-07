# global关键字修饰变量后标识该变量是全局变量，对该变量进行修改就是修改全局变量
# 而nonlocal关键字修饰变量后标识该变量是上一级函数中的局部变量
# 如果上一级函数中不存在该局部变量，nonlocal位置会发生错误

# nonlocal作用于上一层嵌套函数
# global作用于全局

"""
a = 1
def a1():
    a = 2
    def a2():
        nonlocal a
        a+=1
        print('a2',a)
    a2()
    print('a1', a)

a1()
print('a0',a)
"""
# 结果
"""
a2 3
a1 3
a0 1
"""
