"""
Date:2026/4/22 10:41
Author:Jesse

Python入门习题第69练：定义计算器类
需求：定义一个简单的计算器类，这个类支持加、减、乘、除四种基本运算。
"""
#定义计算器类
class Calculator:
    """用于模拟一个计算器，支持加、减、乘、除四种基本运算"""
    def add(self,a,b):
        """
        加法运算
        :param a:
        :param b:
        :return:
        """
        return a+b

    def subtract(self,a,b):
        """
        减法运算
        :param a:
        :param b:
        :return:
        """
        return a-b

    def multiply(self,a,b):
        """
        乘法运算
        :param a:
        :param b:
        :return:
        """
        return a*b

    def divide(self,a,b):
        """
        除法运算
        :param a:
        :param b:
        :return:
        """
        if b==0:
            raise ValueError("除数不能为0")
        return a/b


#示例使用，实例化对象
calculator = Calculator()

print(calculator.add(10, 2))
print(calculator.subtract(10, 2))
print(calculator.multiply(10, 2))
print(calculator.divide(10, 0))




