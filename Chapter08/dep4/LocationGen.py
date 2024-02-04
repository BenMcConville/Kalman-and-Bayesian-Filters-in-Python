from numpy.random import randn
import math

def Noise(z, var):
    return (randn() * var) + z


class Sensor:
    x_pos = 0
    x_vel = 0
    x_acc = 0
    
    y_pos = 0
    y_vel = 0
    y_acc = -9.8

    S_Var = 0
 
    def __init__(self, x, dx, y, dy, SV):
        self.x_pos = x
        self.x_vel = dx

        self.y_pos = y
        self.y_vel = dy

        self.S_Var = SV

    def move(self, epoch):

        ax = (0.0039 + (0.0058/ (1+ math.exp((self.x_vel - 35)/5)))) * (self.x_vel) * -1
        ay = (0.0039 + (0.0058/ (1+ math.exp((self.y_vel - 35)/5)))) * (self.y_vel) * -1      
        

        self.x_pos = (epoch * self.x_vel) + self.x_pos
        self.x_vel = self.x_vel + (ax * epoch * self.x_vel)

        self.y_pos = (epoch**2 * 0.5 * self.y_acc) + (epoch * self.y_vel) + self.y_pos
        self.y_vel = (epoch * self.y_acc) + self.y_vel + (ay * epoch * self.y_vel)
        

    def read(self):
        return (self.x_pos, self.y_pos)
        return (Noise(self.x_pos, self.S_Var), Noise(self.y_pos, self.S_Var))

    
        
