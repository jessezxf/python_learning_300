"""
Date:2026/4/25 13:49
Author:Jesse

Python入门习题第75练：定义在线聊天室类
需求：定义一个简单的在线聊天室类。这个类允许用户加入聊天室、发送消息、查看聊天记录以及离开聊天室。
"""

class ChatRoom:
    """在线聊天室，允许用户加入、离开、发送消息、查看聊天记录"""
    def __init__(self,name):
        self.name = name    #聊天室名称
        self.users = []     #当前聊天室中的用户列表
        self.messages = []  #聊天室中的消息记录

    def jion(self,user):
        """
        用户加入聊天室
        :param user:要加入的用户
        :return:无
        """
        #判断用户是否在用户列表
        if user not in self.users:  #防止重复加入
            #将用户添加到用户列表
            self.users.append(user)
            #添加一条消息记录
            self.messages.append(f"{user}加入了聊天室")

    def leave(self,user):
        """
        用户离开聊天室
        :param user:要离开的用户
        :return:无
        """
        # 判断用户是否在用户列表
        if user in self.users:
            #从用户列表中移除用户
            self.users.remove(user)
            #添加一条消息记录
            self.messages.append(f"{user}离开了聊天室")

    def send_message(self,user,message):
        """
        用户在聊天室中发消息
        :param user:要发送信息的用户
        :param message:要发送的信息内容
        :return:无
        """
        #判断用户是否在用户列表
        if user in self.users:
            #添加一条消息记录
            self.messages.append(f"{user}:{message}")

    def show_message(self):
        """
        显示聊天室中所有的消息记录
        :return:无
        """
        #判断消息列表是否有消息
        if self.messages:
            #遍历消息列表
            for messege in self.messages:
                #打印每条消息
                print(messege)
        else:
            print("聊天室中没有消息记录")


#示例使用
chat_room = ChatRoom("python聊天市1")

#加入聊天室
chat_room.jion("jesse")
chat_room.jion("bingbing")

#发送消息
chat_room.send_message("jesse","大家好！！")
chat_room.send_message("bingbing","欢迎in")
chat_room.send_message("jesse","一起出来玩")

#尝试不存在的用户发言
chat_room.send_message("zizi","出来玩")

#离开聊天市
chat_room.leave("jesse")

#尝试让不在聊天室的用户离开
chat_room.leave("zizi")

#xi显示聊天室中所有消息
chat_room.show_message()


