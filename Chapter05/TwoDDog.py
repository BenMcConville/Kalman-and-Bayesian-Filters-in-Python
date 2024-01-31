import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randn
import math

def Noise(var, val):
    return val + (randn() * var)


class Dog:
    position = (5, 5)
    velocity = (1, 2)
    pVar = 0
    sVar = 0
    
    def __init__(self, processVar, SensorVar):
        self.pVar = processVar
        self.sVar = SensorVar

    def move(self, epoch):
        x, y = self.position
        dx, dy = self.velocity
        
        x = x + (dx * epoch)
        y = y + (dy * epoch)

        x = Noise(self.pVar, x)
        y = Noise(self.pVar, y)


        self.position = (x, y)

    def read(self):
        x, y = self.position
        x = Noise(self.sVar, x)
        y = Noise(self.sVar, y)
        
        self.position = (x, y)
        return (x, y)

class KF:  # KF is just predicting state of x pos & x vel
    epoch = 0.1
    x = np.array([5., 4.5]).T
    P = np.array([[500., 0.],
                  [0., 49.]])
    
    F = np.array([[1., epoch],
                  [0., 1.]]) 

    '''
        Process Model is:
        pos = pos + vel * time
        vel = vel

        Hence
        [pos] = [1, time] [pos]
        [vel]   [0,    1] [vel]
    '''

    def __init__(self):
        print("Initialized...")
    
    def predict(self):
        self.x = np.dot(self.F, self.x) 
        self.P = np.dot(self.F, np.dot(self.P, self.F.T)) + np.dot([[2., 0.], [0., 2.]])
        print(self.x)      
        print(self.P)


Simon = Dog(2., 2.)
pos = []

fil = KF()
fil.predict()


for i in range(50):
    Simon.move(1.)
    pos.append(Simon.read()) 
    


#xx, yy = zip(pos)




plt.scatter(*zip(*pos))
plt.show()
