
#300

# num1 = float(input("输入第一个数："))

# num2 = float(input("输入第二个数："))
# print(f"第一个数{num1}")
# print(f"第二个数{num2}")
# result = num1 + num2
# print(f"{num1}+{num2}={result}")


# while True:
#     """
#     循环计算两数之和
#     """
#     num1 = input("输入第一个数（输入q退出）：")
#     if num1.lower() =='q':
#         print("退出程序")
#         break
#
#     num2 = input("输入第2个数（输入q退出）：")
#     if num2.lower() =='q':
#         print("退出程序")
#         break
#
#     try:
#         num1 = float(num1)
#         num2 = float(num2)
#         result = num1 + num2
#         print(f"{num1}+{num2}={result}\n\n")
#     except ValueError:
#         print("输入有效的数字或输入q退出！！")



def add(num1,num2):
    """
    计算两数之和
    :param num1:第一个数（int 或 float）
    :param num2:
    :return:
    """
    try:
        result = float(num1) + float(num2)
        print(f"{num1}+{num2}={result}\n")
        return result
    except ValueError:
        print("请输入有效的数字")
        return None

add(2,3)

