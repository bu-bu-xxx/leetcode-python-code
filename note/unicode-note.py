"""encode 和 decode
a = '中国'
b1 = a.encode('unicode-escape')
print(b1)
b2 = b1.decode('unicode-escape')
print(b2)

print(a.encode('gbk'))
print(a.encode('gbk').decode('gbk'))

# 我设置了默认utf-8编码
print(a.encode())
print(a.encode().decode())
"""


"""chr() 和 ord()
# ASCII
print(chr(98))
# 16进制，unicode
print(chr(0x28AA))
# 10进制，unicode
print(chr(int("28AA",16)))
"""



