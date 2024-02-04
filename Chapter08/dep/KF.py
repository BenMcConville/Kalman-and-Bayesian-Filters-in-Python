import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randn
import math
from numpy.linalg import inv

class KF:
    epoch = 1.
    
    x = np.array([[0., 0., 0., 0.]]).T # x x_dot y y_dot
    P = np.eye(4) * 500

    F = np.array([[1., epoch, 0, 0],
                  [0., 1., 0., 0. ],
                  [0., 0., 1., epoch],
                  [0., 0., 0., 1.]])

    Q = np.array([[0.   , 0.001, 0.   , 0.   ],
                  [0.001, 0.001, 0.   , 0.   ],
                  [0.   , 0.   , 0.   , 0.001],
                  [0.   , 0.   , 0.001, 0.001]])

    H = np.array([[1., 0., 0., 0.],
                  [0., 0., 1., 0.]])

    R = np.array([[5., 0.],
                  [0., 5.]])

    def __init__(self):
        print("Initilized...")

    def predict(self):
        self.x = np.dot(self.F, self.x)
        self.P = np.dot(self.F, np.dot(self.P, self.F.T))

    def update(self, (x, y)):
        z = np.array([[x, y]]).T
        y = z - np.dot(self.H, self.x)
        A = inv(np.dot(self.H, np.dot(self.P, self.H.T))+ self.R)
        K = np.dot(self.P, np.dot(self.H.T, A))

        self.x = self.x + np.dot(K, y)
        self.P = self.P - np.dot(K, np.dot(self.H, self.P))

    def returnXY(self):
        return (self.x[0], self.x[2])


                



