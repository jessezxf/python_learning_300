"""
Date:2026/5/13 16:01
Author:Jesse

Python入门习题第94练：提取电子邮箱
需求：给定一段包含多个邮箱地址的文本，要求提取出所有标准的邮箱地址。
"""
import re

#示例文本
content ="""
寻隐者12345@qq.com不遇
朝代：唐asdf12dsa#abc.com代
作python666@163.cn者：贾岛
松下问童子，言师python-abc@163com采药去。
只在python_ant-666@sina.net此山中，云深不知处。
"""

#编译一个正则表达式模式，用于匹配标准的邮箱地址
pattern = re.compile(
    r"""
    [0-9a-zA-Z_-]+
    @
    [0-9a-zA-Z_-]+
    \.
    [a-z]{2,4}
    """, re.VERBOSE
)#re.VERBOSE参数用于忽略正则表达式中的空白字符和注释,支持多行编写

# results = re.findall(pattern, content)
results = pattern.findall(content)

for result in results:
    print(result)


