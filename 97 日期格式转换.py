"""
Date:2026/5/13 16:59
Author:Jesse

Python入门习题第97练：日期格式转换
需求：给定一个包含多种日期格式的字符串，要求将其中的日期格式统一转换为YYYY-MM-DD的形式。
"""
import re

#给定字符串，包含不同格式的日期
content ="""
白日依2021/05/26山尽，黄河入2021.05.27海流。
欲穷05-28-2020千里目，更上1/29/2020一层楼。
"""

content = re.sub(r"(\d{4})/(\d{2})/(\d{2})",r"\1-\2-\3",content)

content = re.sub(r"(\d{4})\.(\d{2})\.(\d{2})",r"\1-\2-\3",content)

content = re.sub(r"(\d{2})-(\d{2})-(\d{4})",r"\3-\1-\2",content)

content = re.sub(r"(\d)/(\d{2})/(\d{4})",r"\3-0\1-\2",content)
print(content)