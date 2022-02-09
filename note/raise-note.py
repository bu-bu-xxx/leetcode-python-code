"""
if 1:
    raise ValueError('123')
"""
# 上面的报错会停止运行，并输出报错


"""
try:
    if 1:
        raise ValueError
except ValueError:
    print('123455')

print('2323')
"""
# 上面就会继续运行，try的作用

