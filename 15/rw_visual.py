import matplotlib.pyplot as plt

from random_work import RandomWalk as RW

#程序运行就不断模拟
while True:
    #创建一个RandomWalk实例，并将包含的点都绘制出来
    rw = RW()
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Reds,edgecolors='none',s=1)
    plt.show()

    keep_running = input("Make another walk:(y/n):")
    if keep_running == 'n':
        break