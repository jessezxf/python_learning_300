"""
Date:2026/5/13 17:15
Author:Jesse

Python入门习题第98练：英文分词计算词频
需求：从BeginnerGuideToPython.txt文件中提取单词并统计词频，打印频率最高的前20个单词及其出现次数。
"""
import re
import pandas as pd

#读取文件内容
with open('BeginnerGuideToPython.txt','r',encoding='utf-8') as f:
    content = f.read()

#使用正则表达式分割内容并提取单词
words = re.split(r"[\s?!\.;,]+", content)

#将单词转换为Pandas Series对象
word_series = pd.Series(words)

top_20_words = word_series.value_counts()[:20]

print(top_20_words)



