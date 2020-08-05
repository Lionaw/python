import numpy

x_value = list(numpy.arange(0,100))
y_value = [float(x/1000) for x in x_value]
for y in y_value:
    print('%.3f' % y)