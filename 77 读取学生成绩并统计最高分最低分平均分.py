"""
Date:2026/5/11 15:06
Author:Jesse

Python入门习题第77练：读取学生成绩并统计最高分最低分平均分
需求：从students_grade_file.txt文件中读取学生的成绩数据，
并计算这些成绩中的最高分、最低分以及平均分（平均分需保留两位小数）。
"""
def compute_scores():
    """
    读取学生成绩并统计最高分最低分平均分
    :return: 包含最高分、最低分、平均分的元组
    """
    scores = []
    #读取文件内容
    with open('students_grade_file.txt',encoding="utf-8") as f:
        #遍历文件的每一行
        for line in f.readlines():
            #去除每行末尾的换行符
            line = line[:-1]
            #每行按照，分割
            line = line.split(",")
            #提取成绩并转换为整数添加到列表
            scores.append(float(line[-1]))
    # print(scores)
    #使用max函数计算最高分
    max_score = max(scores)
    #使用min函数计算最低分
    min_score = min(scores)
    #计算平均分
    avg_score = round(sum(scores)/len(scores),2)

    return max_score,min_score,avg_score


#调用函数并接收返回值
max_score,min_score,avg_score = compute_scores()

#打印最高分、最低分、平均分
print(f"最高分：{max_score}，最低分：{min_score}，平均分：{avg_score:.2f}")










