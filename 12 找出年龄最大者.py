"""
Date:2026/4/4 17:52
Author:Jesse

Python入门习题第12练：找出年龄最大者
需求：给定一个字典，其中每个人的姓名作为键，对应的年龄作为值。请找出年龄最大者的姓名与年龄，并将其打印出来。
#定义一个包含姓名和年龄的字典
people ={"张三":18,"李四":50,"王五":29,"赵六":22}
"""

people ={"张三":18,"李四":50,"王五":29,"赵六":22}
max_age = float('-inf')  #将最大年龄初始化为负无穷大，确保任何年龄都会比它大
max_name = ''            # 将最大年龄对应的姓名初始化为空字符

#遍历字典中的每个键值对
for name,age in people.items():
    print(name,end="")
    print(age)
    if age > max_age:
        max_age = age
        max_name = name

print(f"年龄最大者的姓名:{max_name},年龄{max_age}岁")
