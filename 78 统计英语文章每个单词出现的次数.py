"""
Date:2026/5/11 17:40
Author:Jesse

Python入门习题第78练：统计英语文章每个单词出现的次数
需求：编写一个程序，统计指定文本文件中各个单词出现的次数，并将出现次数最多的前十个单词及其对应的次数输出。
"""
#定义字典保存单词及其出现的次数
word_count = {}

#读取文件内容
with open("Englishpaper.txt", "r",encoding="utf-8") as f:
    #遍历文件的每一行
    for line in f.readlines():
        #去除每一行末尾的换行符
        line = line[:-1]
        #将每一行按空格分割成单词列表
        words = line.split()
        #判断列表是否不为空
        if words:
            #遍历单词列表中的每个单词
            for word in words:
                #如果单词不存在于字典中
                if word not in word_count:
                    #将单词添加到字典中，并设置出现次数为1
                    word_count[word] = 1
                else:
                    #如果单词已经存在于字典中，则将出现次数加1
                    word_count[word] += 1

# print("统计单词个数：",word_count)
#对字典进行排序（按照出现次数降序），并获取前十的单词及其对应出现的次数
top_10_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:10]
print("出现次数最多的前十个单词及其对应的次数：",top_10_words)









