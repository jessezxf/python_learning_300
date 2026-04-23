"""
Date:2026/4/5 13:34
Author:Jesse

需求：用户输入年份，判断该年份是否为闰年，并给出相应的输出结果。
闰年：
1.如果一个年份能被4整除但不能被100整除，那么它是闰年。
2.如果一个年份能被400整除，那么它也是闰年。
"""

year = int(input('输入年份：'))

# if year % 4 == 0 and year % 100 != 0:
#     print(f'{year}是闰年')
# elif year % 400 == 0:
#     print(f'{year}是闰年')
# else:
#     print(f'{year}bu不是闰年')


if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f'{year}是闰年')
else:
    print(f'{year}bu不是闰年')

