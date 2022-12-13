a = 10
b = 10.1
c = 5
e = 10.0
print(a < b)
print(a > b)
print(a == e)
# 注意这里是整数和浮点数全等判断，结果为Preprint(a/2 == c)
# 这里使用运算符print(b//1 == e)print(b//2 == c)print(b//2 >= c)print(b//2 != c)print(b is not c)
'''
==	如果两个操作数相等，则返回True，否则返回False。	a == b
！=	如果两个操作数不相等，则返回True，否则返回False。	a！= b
>	如果左操作数大于右操作数，则返回True，否则返回False。	a> b
<	如果左操作数小于右操作数，则返回True，否则返回False。	a <b
> =	如果左操作数大于或等于右操作数，则返回True，否则返回False。	a> b
<=	如果左操作数小于或等于右操作数，则返回True，否则返回False。	a <b
'''
aa = 10
bb = 20
cc = 30
print(aa == bb ,aa >= bb, sep='\n')