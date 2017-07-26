#coding=utf-8
import matplotlib.pyplot as plt

# scatter(),前面参数可以放入数组
x_values = [1,2,3,4,5]
y_values = [1,4,9,16,25]
plt.scatter(x_values,y_values,s=100)
#plt.scatter(2,4,s=200)

# 设置图标的标题并给坐标加上标签
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize = 14)

# 设置刻度表记得大小
"""labelsize是指标签上的字体大小"""
plt.tick_params(axis='both',labelsize=14)
plt.show()
