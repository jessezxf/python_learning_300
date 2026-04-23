# a = float(input("输入第一个数："))
# b = float(input("输入第2个数："))
#
# if a > b:
#     print(f"{a} > {b}")
# elif a == b:
#     print(f"{a} = {b}")

# else:
#     print(f"{a} < {b}")





while True:
    num1 = input("输入第一个数（输入q退出）：")
    if num1.lower() =='q':
        print("退出程序")
        break

    num2 = input("输入第2个数（输入q退出）：")
    if num2.lower() =='q':
        print("退出程序")
        break

    try:
        num1 = float(num1)
        num2 = float(num2)
        if num1 > num2:
            print(f"{num1} > {num2}")
        elif num1 == num2:
            print(f"{num1} = {num2}")
        else:
            print(f"{num1} < {num2}")
    except ValueError:
        print("输入有效的数字或输入q退出！！\n")

