"""
Date:2026/4/20 15:06
Author:Jesse

Python入门习题第49练：随机生成验证码
需求：编写一个程序，该程序能够根据用户指定的长度随机生成一个验证码（可包含大小写英文字母以及数字）。
"""
import string
import random

length = int(input("请输入验证码长度："))

#定义验证码中可能包含的字符集
# string.ascii_letters    #大小写字母
# string.digits           #数字
characters = string.ascii_letters + string.digits
# print(characters)

verify_code = ""
for i in range(length):
    verify_code += random.choice(characters)


print(f"生成的验证码为：{verify_code}")


