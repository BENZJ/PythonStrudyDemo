#coding=utf-8
class Dog():
    """模拟小狗的简单尝试"""

    def __init__(self, name, age):
        """初始化属性和姓名"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令蹲下"""
        print self.name.title(), "is now sitting."

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print self.name.title(), "rolled over!"

mydog = Dog('willie', 6)

mydog.roll_over()

mydog.sit()
