"""
Date:2026/4/25 12:50
Author:Jesse

Python入门习题第74练：定义文本文件处理类
需求：定义一个名为TextFileHandler的类，该类支持文本文件的读取和写入功能。
"""


#定义文本文件处理类
class TextFileHandler:
    """用于处理文本文件的读取和写入操作"""
    def __init__(self,file_path):
        self.file_path = file_path  #文本文件路径

    def read_file(self):
        """
        读取文本文件内容
        :return: 读取到的内容。如果文件不存在，返回“文件不存在”
        """
        try:
            #读取文件内容
            with open (self.file_path,"r",encoding="utf-8") as f:
                content = f.read()
        except FileNotFoundError:
            #如果文件不存在，捕获异常并返回“文件不存在”
            return "文件不存在"
        else:
            #返回读取到的内容
            return content

    def write_file(self,content):
        """
        将内容写入文本文件
        :param content:要写入的内容
        :return:无
        """
        #往文件追加内容
        with open (self.file_path,"a",encoding="utf-8") as f:
            f.write(content + "\n") #追加内容并换行

#示例使用
handle = TextFileHandler("example.txt")

#向文件写入内容
# handle.write_file("hello tongxue nihao")
# handle.write_file("可以加个好友吗%%")
# handle.write_file("明天一起打球吗")
handle.write_file("可以啊")

#读取文件内容
print(handle.read_file())








