import matplotlib.pyplot as plt
import math

from dep.LocationGen import Sensor
from dep.KF import KF
from dep.Rocket import EKF

from numpy.random import randn
import numpy as np


# This section shows the limitiations of linear filters applied to non-linear systems

sensor = Sensor(0, math.cos(math.radians(60))* 500, 0, math.sin(math.radians(60))* 500, 5.)
fil    = KF(0.5)

fil2    = EKF()

previous = (0., 0.)
pos = []
est = []
est2= []
real= []

a,b,c = [], [], []



for i in range(121):
    sensor.move(.1)
    x, z = sensor.read()
    real.append(sensor.returnXY())
    pos.append((x, z))
    #pos.append(z)
    fil2.predict(.1)
    fil2.update((x, randn(), z))

    est2.append((fil2.x[0][0], fil2.x[2][0]))
    #est2.append(fil2.get())

plt.plot(*zip(*est2), c='red')
plt.plot(*zip(*pos))
plt.plot(*zip(*real), c='black')
#plt.plot(pos)
#plt.plot(est)
#plt.plot(est2)


plt.show()







