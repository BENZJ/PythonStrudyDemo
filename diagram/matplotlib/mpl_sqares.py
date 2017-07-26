#coding=utf-8
import matplotlib.pyplot as plt

squares = [1,4,9,16,25]
input_values = [1,2,3,4,5]
# linewidth可以用来表示线条粗细

"""默认情况下plt输出若不定下x坐标认为是下表0,1,.....   所以下图输出的并不是正确的平方"""
#plt.plot(squares,linewidth=5)
plt.plot(input_values,squares,linewidth=5)



# 设置图标的标题并给坐标加上标签
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize = 14)

# 设置刻度表记得大小
"""labelsize是指标签上的字体大小"""
plt.tick_params(axis='both',labelsize=14)
plt.show()
