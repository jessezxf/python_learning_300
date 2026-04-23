"""
Date:2026/4/22 10:56
Author:Jesse

Python入门习题第70练：子类重写父类方法
需求：
1.定义一个父类Vehicle，包含一个方法describe，用于描述车辆的基本信息。
2.定义一个子类Car，继承自Vehicle，并重写describe 方法，以提供关于汽车的特定信息。
"""
#定义父类
class Vehicle:
    """车辆类"""
    def __init__(self, make, model):
        self.make = make        #品牌
        self.model = model      #型号

    def describe(self):
        """
        描述车辆信息

        返回值：车辆描述
        """
        return f"车辆品牌：{self.make}，型号：{self.model}"



#定义子类，继承自Vehicle类
class Car(Vehicle):
    """汽车类，继承自车辆类"""
    def __init__(self,year,make, model):
        super().__init__(make, model)   #调用父类构造函数来初始化品牌和型号
        self.year = year        #汽车年份

    #重写父类方法
    def describe(self):
        """
        描述汽车信息

        返回值：汽车描述
        """
        return f"汽车年份：{self.year},车辆品牌：{self.make}，型号：{self.model}"



#示例使用
#实例化子类对象
car = Car("2025", "Tesla", "Model S")

#描述汽车的基本信息
print(car.describe())










