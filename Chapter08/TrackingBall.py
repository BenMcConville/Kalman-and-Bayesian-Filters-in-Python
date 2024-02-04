import matplotlib.pyplot as plt
import math

from dep4.LocationGen import Sensor
from dep4.KF import KF


# This section shows the limitiations of linear filters applied to non-linear systems

sensor = Sensor(0, math.cos(math.radians(60))* 100, 0, math.sin(math.radians(60))* 100, 2.)
fil    = KF(0.5)

pos = []
est = []

for i in range(25):
    sensor.move(.5)
    z = sensor.read()

    pos.append(z)

    fil.predict()
    fil.update(z)
    est.append(fil.returnXY())

plt.plot(*zip(*est))
plt.scatter(*zip(*pos))
plt.ylim(0, 250)
plt.show()

