"""
Date:2026/4/20 11:10
Author:Jesse

Python入门习题第44练：验证年龄
需求：定义一个函数，该函数接收一个人的年龄作为参数。如果年龄不在合法范围内（比如小于0或大于120），则抛出异常。
"""

def verify_age(age):
    """
    验证年龄是否在合法范围内
    :param age: 要验证的年龄
    :return: 合法年龄
    """
    if age < 0 or age > 120:
        #抛出自定义异常 ==> raise 异常类型(异常具体描述信息)
        raise Exception("年龄必须在0到120岁之间~~")
    return age


print(verify_age(18))
try:
    print(verify_age(180))
except Exception as e:
    print(e)
print(verify_age(23))

