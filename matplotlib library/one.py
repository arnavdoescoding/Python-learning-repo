from cProfile import label
from matplotlib import pyplot as pyp

dev_x =[ 1 ,2 ,3, 4, 5, 6, 7]
dev_y = [23, 31, 52, 12, 10 , 11 , 2]
dev_z = [100 , 2, 23, 45, 12 , 91 , 0]
pyp.plot(dev_x , dev_y , label= 'All Devs')
pyp.plot(dev_x , dev_z  , label= 'Python')
pyp.title('First Matplot(1)')
pyp.xlabel('X-Axis')
pyp.ylabel('Y-Axis')
pyp.legend()
pyp.tight_layout()
pyp.grid(True)
pyp.show()
pyp.savefig('sample.png')