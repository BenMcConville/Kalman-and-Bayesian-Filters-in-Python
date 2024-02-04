import matplotlib.pyplot as plt
import math

from dep.LocationGen import Sensor
from dep.KF import KF


sensor = Sensor((50., 50.), 2.)
fil = KF()


pos = []
guess = []

for i in range(20):
    fil.predict() 
    z = sensor.read()

    fil.update(z)
    
    guess.append(fil.returnXY())
    x, y = fil.returnXY()
    pos.append(z)


#plt.plot(*zip(*guess))
plt.scatter(*zip(*guess))
plt.scatter(*zip(*pos))
plt.show()
print(fil.P)
