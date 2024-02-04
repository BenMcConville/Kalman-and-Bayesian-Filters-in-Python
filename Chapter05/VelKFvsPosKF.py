import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randn
import math
from numpy.linalg import inv



def Noise(var, val):
    return val + (randn() * var)


class Dog:
    position = (5, 5)
    velocity = (.5, .5)
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
    epoch = 1.
    x = np.array([[5., 4.5]]).T
    P = np.array([[500., 0.],
                  [0., 49.]])
    
    F = np.array([[1., epoch],
                  [0., 1.]]) 
    
    H = np.array([[1, 0]]) # Measurement
    R = np.array([[5.]])
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
        self.P = np.dot(self.F, np.dot(self.P, self.F.T)) + np.array([[2., 0.], [0., 2.]])

    def update(self, z):
        y = z - np.dot(self.H, self.x)
        A = inv((np.dot(self.H, np.dot(self.P, self.H.T)) + self.R).reshape(1,1))
        K = np.dot(self.P, np.dot(self.H.T,A)) 
        
        self.x = self.x + np.dot(K, y)
        self.P = self.P - np.dot(K, np.dot(self.H, self.P))


class KF2:  # KF is just predicting state of x pos & x vel
    epoch = 1.
    x = np.array([[5.]])
    P = np.array([[500.]])
    
    F = np.array([[1.]]) 
    
    H = np.array([[1.]]) # Measurement
    R = np.array([[5.]])
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
        self.P = np.dot(self.F, np.dot(self.P, self.F.T)) + np.array([[2.]])

    def update(self, z):
        y = z - np.dot(self.H, self.x)
        A = inv((np.dot(self.H, np.dot(self.P, self.H.T))+self.R).reshape(1,1))
        K = np.dot(self.P, np.dot(self.H.T,A)) 
        
        self.x = self.x + np.dot(K, y)
        self.P = self.P - np.dot(K, np.dot(self.H, self.P))

Simon = Dog(.5, .5)
pos = []
est = []
est2 = []

fil = KF()
fil2 = KF2()

for i in range(50):
    Simon.move(1.)
    x, y = Simon.read()
    fil2.predict()
    fil2.update(np.array([y]))
    est2.append(fil2.x[0])    

    fil.predict()
    fil.update(np.array([y]))
    print(fil.x[0])
    est.append(fil.x[0])

    # pos.append((x, y)) # X-Y Positions
    pos.append((1.*i, y)) # Y-time Position
    




plt.plot(est)
plt.plot(est2)
plt.scatter(*zip(*pos))
plt.show()
