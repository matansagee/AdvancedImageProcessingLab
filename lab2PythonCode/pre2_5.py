import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from scipy import interpolate
from scipy.interpolate import RectBivariateSpline
from matplotlib.ticker import LinearLocator, FormatStrFormatter

def gf (x,y,r):
    return math.exp(-(pow(x,2)+pow(y,2))/(2*pow(r,2)))

a = np.empty((12,12));
a = a*0;
x = np.ones(12);
x = x*255;
for i in range(0,6):
    a[:,i] = x;
p = np.zeros((5,5));
i0 = 4;
j0 = 7;
print "pos ({},{})".format(i0+2,j0+2);
for i in range(0,5):
    for j in range(0,5):
        x = i-2;
        y = j-2;
        gs = gf(x,y,10);
        x = a[i0+i,j0+j]-a[i0+2,j0+2];
        y = 0;
        gr = gf(x,y,10);
        p[i,j] = gs*gr;



np.set_printoptions(precision=4);
np.set_printoptions(suppress = True);
print p

x = y = np.arange(-2,3);
f = interpolate.interp2d(x, y, p, kind='cubic')

x2 = y2 = np.arange(-2,3,0.1);
X2, Y2 = np.meshgrid(x2,y2)
Z2 = f(y2, x2)


fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X2, Y2, Z2, rstride=1, cstride=1, cmap=cm.coolwarm,
                linewidth=0, antialiased=False)
ax.set_zlim(0,1)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

plt.show()

