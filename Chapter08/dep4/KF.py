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

    B = np.array([[ 0., 0., 0., 0.5 * -9.8]]).T

    Q = np.array([[0.2 , -0.3, 0.1 , 0.1],
                  [0.1 , 0.1 , 0.4 ,-0.1],
                  [-0.3, 0.05, -0.2, 0.4],
                  [-0.2, -0.4, -0.2, 0.4]])

    H = np.array([[1., 0., 0., 0.],
                  [0., 1., 0., 0.]])

    R = np.array([[0.5, 0  ],
                  [0. , 0.5]])

    def __init__(self, dt):
        print("Initilized...")
        self.epoch = dt

    def predict(self):
        self.x = np.dot(self.F, self.x) + self.B
        self.P = np.dot(self.F, np.dot(self.P, self.F.T))# + self.Q

    def update(self, (x, y)):
        '''if (self.x[0] + self.GATE_LIMIT * self.P[0][0] < x): 
            print("Gating")
            return 0
        '''
        z = np.array([[x, y]]).T
        y = z - np.dot(self.H, self.x)
        A = inv(np.dot(self.H, np.dot(self.P, self.H.T))+ self.R)
        K = np.dot(self.P, np.dot(self.H.T, A))

        self.x = self.x + np.dot(K, y)
        self.P = self.P - np.dot(K, np.dot(self.H, self.P))

    def returnXY(self):
        return ((self.x[0], self.x[1]))


                



