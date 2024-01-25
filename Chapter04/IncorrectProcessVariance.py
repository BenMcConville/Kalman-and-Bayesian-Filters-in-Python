import matplotlib.pyplot as plt
from numpy.random import randn
import math


speed = 5.

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
    speed = 5.    

    def __init__(self, pv, sv, pos):
        self.process_var = pv
        self.sensor_var  = sv
        self.position    = pos

    def move(self, epoch):
        self.speed = self.speed + 0.5
        self.position = self.position + (epoch * self.speed)
        self.position += randn() * self.process_var/2# Add Process Noise

    def getSensor(self):
        return self.position + randn() * self.sensor_var/2

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



Simon = dog(1., 1.0, 0.)
Filter = KF(0.005, 1.0, 400.)

points = []

a, b, c = [], [], []
low, upp = [], []

for i in range(100):
    #plotDis(Filter.mean, Filter.var)
    Simon.move(1.)
    
    Filter.posPredict(1.)

    z = Simon.getSensor()
    a.append(z)
    b.append(Filter.mean)

    Filter.posUpdate(z)

    c.append(Filter.mean)
    low.append(Filter.mean - Filter.var)
    upp.append(Filter.mean + Filter.var)


plt.plot(range(len(a)),a, '*')
plt.plot(range(len(b)),b, 'o')
plt.plot(c)
plt.fill_between(range(len(c)), low, upp,facecolor='yellow', alpha=0.5)
#plt.ylim(-20,30)
plt.show()



#plotPoints(points)

#plotDis(10,1)















