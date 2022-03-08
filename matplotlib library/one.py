from cProfile import label
from matplotlib import pyplot as plt


x_list = list()
y_list = list()
for x in range(-1000 , 1000):
    x_list.append(x)
    y = (3/5*(x**2/3)) - (((1 - (x**2))**1/2)/2)
    y_list.append(y)

plt.plot(x_list , y_list)
plt.xlabel('Vaish')
plt.ylabel('Arnav')
plt.title('I LOVE YOU!!')

plt.show()






