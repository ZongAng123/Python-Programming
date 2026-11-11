"""
Author: zongang zongang15@yahoo.com
Date: 2026-11-05 14:42:09
LastEditors: zongang zongang15@yahoo.com
LastEditTime: 2026-11-05 14:42:09
FilePath: 第一章/第1章-起步/hello_world.py
Description: 这是默认设置,可以在设置》工具》File Description中进行配置
"""

# 2.1 运行 hello_world.py 时发生的情况
print("Hello Python world!")


# 2.2 变量
# 下面来尝试在hello_world.py中使用一个变量。在这个文件开头添加一行代码，并对第2行代码进行修改，如下所示：
message = "Hello Python world!"
print('-------',message)
"""
我们添加了一个名为message的变量。每个变量都存储了一个值——与变量相关联的信息。
在这里，存储的值为文本“Hello Python world!”
"""
message = "Hello Python Crash Course world!"
print('-------01',message)
# 在程序中可随时修改变量的值，而Python将始终记录变量的最新值

# 2.2.1 变量的命名和使用
"""
1、变量名只能包含字母、数字和下划线。变量名可以字母或下划线打头，但不能以数字打头，例如，可将变量命名为message_1，但不能将其命名为1_message。
2、变量名不能包含空格，但可使用下划线来分隔其中的单词。例如，变量名greeting_message可行，但变量名greeting message会引发错误
3、不要将Python关键字和函数名用作变量名，即不要使用Python保留用于特殊用途的单词，如print。
4、变量名应既简短又具有描述性。例如，name比n好，student_name比s_n好，name_length比length_of_persons_name好。
5、慎用小写字母l和大写字母O，因为它们可能被人错看成数字1和0
"""

# 2.2.2 使用变量时避免命名错误
# message = "Hello Python Crash Course reader!"
# print(mesage)

# 2.3 字符串
"""
字符串就是一系列字符。在Python中，用引号括起的都是字符串，其中的引号可以是单引号，
也可以是双引号，如下所示：
"This is a string."
'This is also a string.' 
"""

