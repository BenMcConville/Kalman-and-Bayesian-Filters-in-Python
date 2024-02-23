import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randn
import math
from numpy.linalg import inv

class KF:
    GATE_LIMIT = 40

    epoch = 0.5
    
    x = np.array([[0., 0., 0., 0.]]).T # x y x_dot y_dot
    P = np.eye(4) * 50

    F = np.array([[1., 0.   , epoch, 0.   ],
                  [0., 1.   , 0.   , epoch],
                  [0., 0.   , 1.   , 0.   ],
                  [0., 0.   , 0.   , 1.   ]])

    B = np.array([[ 0., 0., 
        (-epoch * x[2]**2 * (0.0039 + (0.0058 / (1 + math.exp((x[2] - 35)/5))))),
        (-epoch * x[3]**2 * (0.0039 + (0.0058 / (1 + math.exp((x[3] - 35)/5))))) + (epoch * -9.8)]]).T

    '''
    Q = np.array([[0.2 , -0.3, 0.1 , 0.1],
                  [0.1 , 0.1 , 0.4 ,-0.1],
                  [-0.3, 0.05, -0.2, 0.4],
                  [-0.2, -0.4, -0.2, 0.4]])
    '''
    Q = 220.
    H = np.array([[1., 0., 0., 0.],
                  [0., 1., 0., 0.],
                  [0., 0., 1., 0.],
                  [0., 0., 0., 1.]])

    R = np.array([[0.5, 0. , 0., 0.],
                  [0. , 0.5, 0., 0.],
                  [0., 0., 25.25, 0.],
                  [0., 0., 0., 25.25]])

    def __init__(self, dt):
        print("Initilized...")
        self.epoch = dt

    def predict(self):
	B = np.array([[ 0., 0., 
        (-self.epoch * self.x[2]**2 * (0.0039 + (0.0058 / (1 + math.exp((self.x[2] - 35)/5))))), 
        (-self.epoch * self.x[3]**2 * (0.0039 + (0.0058 / (1 + math.exp((self.x[3] - 35)/5))))) + (-9.8 * self.epoch)]]).T
        self.x = np.dot(self.F, self.x) + self.B
        self.P = np.dot(self.F, np.dot(self.P, self.F.T))# + self.Q

    def update(self, (x, y), (dx, dy)):
        '''if (self.x[0] + self.GATE_LIMIT * self.P[0][0] < x): 
            print("Gating")
            return 0
        '''
        z = np.array([[x, y, dx, dy]]).T
        y = z - np.dot(self.H, self.x)
        A = inv(np.dot(self.H, np.dot(self.P, self.H.T))+ self.R)
        K = np.dot(self.P, np.dot(self.H.T, A))

        self.x = self.x + np.dot(K, y)
        self.P = self.P - np.dot(K, np.dot(self.H, self.P))

    def returnXY(self):
        return ((self.x[0], self.x[1]))


                



