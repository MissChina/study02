"""             重点
print()函数用于向控制台中输出数据，它可以输出任何类型的数据，其语法格式如下所示：
print(*objects, sep=' ', end='\n', file=sys.stdout)
objects：表示输出的对象。输出多个对象时，对象之间需要用分隔符分隔。
sep：用于设定分隔符，默认使用空格作为分隔。
end：用于设定输出以什么结尾，默认值为换行符\n。
file：表示数据输出的文件对象。
"""

# print(*object,sep='',end='\n',file=sys.stdout)
'''
object：表示输出的对象。输出多个对象时，对象之间用分隔符分隔
sep：用于设定分隔符，默认使用空格作为分隔
end：用于设定输出以什么结尾，默认值为换行符\n
file：表示数据输出的文件对象
'''     # 注释

chinese = '通用名称：阿莫西林胶囊'
english = "英文名称：Amoxicillin Capsules"
character = '性状：本品内容物为白色'
print(chinese+'\n'+english+'\n'+character)

import sys

name = input('请输入你的名字:'+"\n")
"""
input()函数用于接收用户键盘输入的数据，返回一个字符串类型的数据，其语法格式如下所示：
input([prompt])
prompt表示函数的参数，用于设置接收用户输入时的提示信息。
"""     # 注释
print(name)


"Python中内置了用于转换数据进制的函数：bin()、oct()、int()、hex()"         # 注释
a = bin(10)
b = oct(10)
c = str(10)
d = hex(10)
print(a+'\n'+b+'\n'+c+'\n'+d)

















