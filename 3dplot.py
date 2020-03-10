from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

fig = plt.figure()
ax = Axes3D(fig)

x = [6,3,6,9,12,24]
y = [3,5,78,12,23,56]
# put 0s on the y-axis, and put the y axis on the z-axis
ax.plot(xs=x, ys=[0]*len(x), zs=y, zdir='z', label='ys=0, zdir=z')
plt.show()