"""
Date:2026/4/24 10:51
Author:Jesse

Python入门习题第73练：定义在线购物车类
需求：定义一个简单的在线购物车类。这个类支持添加商品、删除商品、查看购物车内容以及计算总价的功能。
"""
#定义在线购物车类
class ShoppingCart:
    """用于模拟一个简单的在线购物车，支持添加商品、删除商品、查看购物车内容及计算总价的功能"""
    def __init__(self):
        """初始化购物车对象"""
        self.cart = {}  #购物车，初始化为空字典，键为商品名称，值为包含数量和单价的字典

    def add_product(self,product_name,quantity,price):
        """
        添加商品到购物车
        :param self: product_name(商品名称),quantity(商品数量),price(商品单价)
        :return: 无
        """
        #判断商品是否已经存在
        if product_name in self.cart:
            #增加数量
            self.cart[product_name]["quantity"] += quantity
        else:
            #添加新商品到购物车
            self.cart[product_name] = {"quantity":quantity,"price":price}

    def remove_product(self,product_name,quantity=None):
        """
        从购物车中删除指定商品或指定数量的商品
        :param self:product_name(要删的商品名称),quantity(要删的商品数量，若为None则删除所有该商品)
        :return:无
        """
        #判断商品是否已经存在
        if product_name in self.cart:
            #判断指定数量是否为None或是否超过实际数量
            if quantity is None or quantity >= self.cart[product_name]["quantity"]:
                #删除所有该商品
                del self.cart[product_name]
            else:
                #减少指定商品的数量
                self.cart[product_name]["quantity"] -= quantity
        else:
            print(f"商品{product_name}不存在！！！")

    def view_cart(self):
        """
        查看购物车内容
        :return: 无
        """
        #判断购物车是否为空
        if not self.cart:
            print("购物车是空的！！！")
        else:
            #遍历购物车中的商品
            for product_name,detail in self.cart.items():
                print(f"商品名称：{product_name}，数量：{detail["quantity"]}，单价：{detail["price"]}元")


    def calculate_total(self):
        """
        计算购物车中所有商品的总价
        :return:total(所有商品的总价)
        """
        #定义变量保存总价
        total = 0

        #遍历购物车中的商品
        for product_name,detail in self.cart.items():
            #累加计算每个商品的总价
            total += detail["quantity"] * detail["price"]
        #返回总价
        return total



#示例使用
#实例化对象
cart = ShoppingCart()

#添加商品
cart.add_product("苹果",2,3)
cart.add_product("香蕉",1,5)

#查看购物车内容
cart.view_cart()

#计算总价
print(f"总价：{cart.calculate_total()}元")


#删除指定数量的商品
cart.remove_product("苹果",1)

#查看购物车内容
cart.view_cart()

#计算总价
print(f"总价：{cart.calculate_total()}元")



cart.add_product("苹果",3,3)
cart.view_cart()
cart.remove_product("苹果")
cart.view_cart()