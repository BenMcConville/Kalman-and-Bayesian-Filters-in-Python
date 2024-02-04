import matplotlib.pyplot as plt
import math

from dep2.LocationGen import Sensor
from dep2.KF import KF


sensor = Sensor(0., 2., 1., 15.)
fil = KF(1.)


pos = []
guess = []

for i in range(40):
    fil.predict() 
    z = sensor.read(1)
    if (i == 25):
        z = z * 1.2
    fil.update(z)
    
    guess.append(fil.returnXY())
    x = fil.returnXY()
    pos.append(z)


#plt.plot(*zip(*guess))
#plt.scatter(*zip(*guess))
#plt.scatter(*zip(*pos))
plt.scatter(range(len(pos)), pos)
plt.plot(guess)
plt.show()
print(fil.P)
