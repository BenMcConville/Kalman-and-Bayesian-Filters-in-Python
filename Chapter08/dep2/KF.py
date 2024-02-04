import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randn
import math
from numpy.linalg import inv

class KF:
    GATE_LIMIT = 4

    epoch = 0.1
    
    x = np.array([[10., 0., 0.]]).T # x x_dot x_dotdot
    P = np.eye(3) * 500

    F = np.array([[1., epoch, 0.5*epoch**2],
                  [0., 1.   , epoch       ],
                  [0., 0.   , 1.          ]])

    Q = np.array([[0.2 , -0.3, 0.1 ],
                  [0.1 , 0.1 , 0.4 ],
                  [-0.3, 0.05, -0.2]])

    H = np.array([[1., 0., 0.]])

    R = np.array([[15.]])

    def __init__(self, dt):
        print("Initilized...")
        self.epoch = dt

    def predict(self):
        self.x = np.dot(self.F, self.x)
        self.P = np.dot(self.F, np.dot(self.P, self.F.T)) + self.Q

    def update(self, x):
        if (self.x[0] + self.GATE_LIMIT * self.P[0][0] < x): 
            print("Gating")
            return 0
        z = np.array([[x]]).T
        y = z - np.dot(self.H, self.x)
        A = inv(np.dot(self.H, np.dot(self.P, self.H.T))+ self.R)
        K = np.dot(self.P, np.dot(self.H.T, A))

        self.x = self.x + np.dot(K, y)
        self.P = self.P - np.dot(K, np.dot(self.H, self.P))

    def returnXY(self):
        return (self.x[0])


                



