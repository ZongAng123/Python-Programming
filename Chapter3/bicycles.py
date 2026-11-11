"""
Author: zongang zongang15@yahoo.com
Date: 2026-11-11 15:56:42
LastEditors: zongang zongang15@yahoo.com
LastEditTime: 2026-11-11 15:56:42
FilePath: Chapter3/bicycles.py
Description: 这是默认设置,可以在设置》工具》File Description中进行配置
"""

"""
列表由一系列按特定顺序排列的元素组成。你可以创建包含字母表中所有字母、数字0~9或所有家庭成员姓名的列表；也可以将任何东西加入列表中，其中的元素之间可以没有任何关系。
鉴于列表通常包含多个元素，给列表指定一个表示复数的名称（如letters、digits或names）是个不错的主意。
"""

"""
在Python中，用方括号（[]）来表示列表，并用逗号来分隔其中的元素。
下面是一个简单的列表示例，这个列表包含几种自行车：
"""

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print('列表----',bicycles)
# 如果你让Python将列表打印出来，Python将打印列表的内部表示，包括方括号：
# ['trek', 'cannondale', 'redline', 'specialized']

# 3.1.1 访问列表元素
"""
列表是有序集合，因此要访问列表的任何元素，只需将该元素的位置或索引告诉Python即可。
要访问列表元素，可指出列表的名称，再指出元素的索引，并将其放在方括号内。
"""
# 例如，下面的代码从列表bicycles中提取第一款自行车：
bicyclesone = ['trek', 'cannondale', 'redline', 'specialized']
print('提取第一款自行车---',bicyclesone[0])