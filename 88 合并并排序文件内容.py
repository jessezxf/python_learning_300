"""
Date:2026/5/13 10:45
Author:Jesse

Python入门习题第88练：合并并排序文件内容
需求：有两个磁盘文件test1.txt和test2.txt，各自存储着一行字母。要求将这两个文件中的字母合并，并按字母顺序进
行排序，然后将排序后的结果写入到一个新的文件test3.txt中。
"""
def read_file(file_path):
    """
    读取文件内容
    :param file_path:要读取的文件路径
    :return: 文件内容
    """
    #读取文件内容
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    return content

content1 = read_file('test1_88.txt')
content2 = read_file('test2_88.txt')

combined_content = content1 + content2
sorted_content = "".join(sorted(combined_content))

#写入新文件
with open('test3_88.txt', 'w', encoding='utf-8') as f:
    f.write(sorted_content)
