"""
Date:2026/4/22 11:28
Author:Jesse

Python入门习题第71练：定义银行账户类
需求：定义一个简单的银行账户类，这个类支持存款和取款操作。
"""

#定义银行账户类
class BankAccount:
    """用于模拟一个简单的银行账户，支持存款和取款操作"""
    def __init__(self,owner,balance=0):
        """初始化账户信息"""
        self.owner = owner          #账户持有者
        self.balance = balance      #账户余额，初始化为0


    def deposit(self,amount):
        """
        存款操作
        参数：amount：存款金额
        返回值：无
        """
        #判断要存入的金额是否为正数
        if amount > 0:
            self.balance += amount
        else:
            print("存款金额必须为正数！")


    def withdraw(self,amount):
        """
        取款操作
        参数：amount：取款金额
        返回值：无
        """
        #判断要取出的金额是否小于等于账户余额
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        else:
            print("取款失败，取款金额必须为正数且不能大于账户余额！")


    def get_balance(self):
        """
        获取账户余额
        参数：无
        返回值：账户余额
        """
        return self.balance

#示例使用
#实例化对象
account = BankAccount("jesse",100)

print("账户余额：",account.get_balance())

#存款操作
account.deposit(200)
print("账户余额：",account.get_balance())

#取款操作
account.withdraw(50)
print("账户余额：",account.get_balance())

account.deposit(-200)







