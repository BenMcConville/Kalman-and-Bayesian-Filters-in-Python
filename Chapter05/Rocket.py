import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randn
import math
from numpy.linalg import inv

def Noise(var, val):
    return val + (randn() * var)

class Rocket():
    P_Var = 5.
    S_Var = 3.
    acc = -9.8
    pos = 0.
    vel = 0.

    def __init__(self, position, velocity):
        self.pos = position
        self.vel = velocity

    def epoch(self, t):
        self.vel = (self.acc * t) + self.vel + Noise(self.P_Var, 0)
        self.pos = (self.vel * t) + self.pos + Noise(self.P_Var, 0)

    def read(self):
        return Noise(self.S_Var, self.pos)

class KF:
    epoch = 1.
    x = np.array([[500., 0., -9.8]]).T
    
    F = np.array([[1., epoch, 0],
                  [0., 1., epoch],
                  [0., 0., 1.]])

    P = np.array([[500., 0., 0.],
                  [0., 9000., 0.],
                  [0., 0., 10.]])

    H = np.array([[1., 0., 0.]])

    R = np.array([[50.]])
    
    def __init__(self):
        print("Initialized...")
    
    def predict(self):
        self.x = np.dot(self.F, self.x) 
        self.P = np.dot(self.F, np.dot(self.P, self.F.T)) + np.array([[2., 0., 0.], [0., 2., 0.], [0., 0., 2.]])

    def update(self, z):
        y = z - np.dot(self.H, self.x)
        A = inv(np.dot(self.H, np.dot(self.P, self.H.T) + self.R).reshape((1,1)))
        
        K = np.dot(self.P, np.dot(self.H.T,A)) 
        
        self.x = self.x + np.dot(K, y)
        self.P = self.P - np.dot(K, np.dot(self.H, self.P))
    
ADA = Rocket(0., 400.)
fil = KF()

z = []
est = []

for i in range(10):
    ADA.epoch(1.)
    y = ADA.read()
    z.append(y)
    fil.predict()
    fil.update(np.array([[y]]))
    print(fil.x[0])
    est.append(fil.x[0])



plt.plot(z)
plt.plot(est)
plt.show() 
