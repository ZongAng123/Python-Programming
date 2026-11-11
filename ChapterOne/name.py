"""
Author: zongang zongang15@yahoo.com
Date: 2026-11-11 09:29:19
LastEditors: zongang zongang15@yahoo.com
LastEditTime: 2026-11-11 09:29:19
FilePath: ChapterOne/name.py
Description: 这是默认设置,可以在设置》工具》File Description中进行配置
"""
# 2.3.1 使用方法修改字符串的大小写
# 对于字符串，可执行的最简单的操作之一是修改其中的单词的大小写。请看下面的代码，并尝试判断其作用：

name = "zongang"
print(name.title())  # Ada Lovelace

"""
在这个示例中，小写的字符串"ada lovelace"存储到了变量name中
在print()语句中，方法title()出现在这个变量的后面。方法是Python可对数据执行的操作。
"""

# 还有其他几个很有用的大小写处理方法。例如，要将字符串改为全部大写或全部小写，可以像下面这样做：
name = "Ada Lovelace"
print(name.upper()) #ADA LOVELACE
print(name.lower()) #ada lovelace

"""
存储数据时，方法lower()很有用。很多时候，你无法依靠用户来提供正确的大小写，因此需要将字符串先转换为小写，再存储它们。
以后需要显示这些信息时，再将其转换为最合适的大小写方式。
"""

