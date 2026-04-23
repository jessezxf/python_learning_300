# 需求：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

s = input("请输入一串字符：")

letter = 0
space = 0
digit = 0
others = 0


#遍历字符
for c in s:
    #判断是否是英文字母
    if c.isalpha():
        letter += 1
    #判断是否是空格
    elif c.isspace():
        space += 1
    #判断是否是数字
    elif c.isdigit():
        digit += 1
    else:
        others += 1

print(f"英文字符{letter}个，空格字符{space}个，数字字符{digit}个，其他字符{others}个")
