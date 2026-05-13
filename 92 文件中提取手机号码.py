"""
Date:2026/5/13 15:11
Author:Jesse

Python入门习题第92练：文件中提取手机号码
需求：从webpage_phone_numbers.txt文件中提取并输出所有符合格式的中国手机号码。
"""
import re


#定义正则表达式模式，用于匹配中国手机号码
#中国手机号码格式：以1开头，第二位是3-9之间的数字，后面有9位数字，一共11位数字
pattern = r"1[3-9]\d{9}"

#打开文件，读取文件内容
with open("webpage_phone_numbers.txt", "r",encoding="utf-8") as f:
    file_content = f.read()
    # print(file_content)

#使用正则表达式匹配手机号码
results = re.findall(pattern, file_content)

for result in results:
    print(result)