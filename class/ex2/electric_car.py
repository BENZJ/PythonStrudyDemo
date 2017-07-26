#coding=utf-8
from car import Car
class ElectricCar(Car):
    """电动汽车"""

    def __init__(self, make,model,year,size):
        """初始化父类的属性"""

        #super().__init__(make,model,year) #在python2.7前这样可以写
        #python2.7中的写法
        super(ElectricCar,self).__init__(make,model,year)
        self.battery_size = size
    def describe_bettery(self):
        """打印一条描述电瓶容量的消息"""
        print "This car has a " + str(self.battery_size)+ "-KWh battery."
