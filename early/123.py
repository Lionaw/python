##https://github.com/ehmatthes/pci
import math
import numpy
from matplotlib import pyplot as plt

print("hello world!")
a=[]
a=range(1,7)
print(a)
x_value = list(numpy.arange(0,100,0.1))
y_value =[float(abs(0.5*x*math.sin(0.1*x))) for x in x_value]
print(y_value)

plt.plot(x_value,y_value,c="red")
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)
plt.savefig("123.png")