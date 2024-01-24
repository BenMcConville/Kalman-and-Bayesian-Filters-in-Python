import matplotlib.pyplot as plt
from numpy.random import randn
import math


speed = 10.

def predict(m1, v1, m2, v2):
    return (m1 + m2, v1 + v2)
    
def update(m1, v1, m2, v2):
    avgMean = ((m2 * v1) + (m1 * v2)) / (v1 + v2)
    avgVar  = (v1 * v2) / (v1 + v2)
    return (avgMean, avgVar)

class dog:
    process_var = 0.
    sensor_var  = 0.
    position    = 0.

    def __init__(self, pv, sv, pos):
        self.process_var = pv
        self.sensor_var  = sv
        self.position    = pos

    def move(self, epoch):
        self.position = self.position + (epoch * speed)
        self.position += randn() * self.process_var# Add Process Noise

    def getSensor(self):
        return self.position + randn() * self.sensor_var / 2.

class KF:
    mean = 0.
    var  = 0.
    process_var = 0.
    sensor_var  = 0.

    def __init__(self, pv, sv, startVar):
        self.process_var = pv
        self.sensor_var  = sv
        self.var         = startVar

    def posPredict(self, epoch):
        self.mean, self.var = predict(self.mean, self.var, speed * epoch, self.process_var)
    
    def posUpdate(self, z):
        self.mean, self.var = update(self.mean, self.var, z, self.sensor_var)


def plotDis(mean, stan):
    x = [mean + i/10. for i in range(-100, 100)]
    y = []
    for i in x:
        val = 2.713**((-(i - mean)**2)/(2*(stan**2))) /(stan* math.sqrt(2*3.14159))
        y.append(val)
    plt.xlim(-10, 200)
    plt.ylim(0, 3)
    plt.plot(x, y)
    plt.show()

def plotPoints(y):
    plt.plot(y)
    plt.show()



Simon = dog(4., 4., 0.)
Filter = KF(4., 4., 10.)

points = []
for i in range(10):
    print(Filter.mean, Filter.var)
    plotDis(Filter.mean, Filter.var)
    Simon.move(1.)
    Filter.posPredict(1.)
    Filter.posUpdate(Simon.getSensor())

#plotPoints(points)

#plotDis(10,1)















