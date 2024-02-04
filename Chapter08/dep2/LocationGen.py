from numpy.random import randn

def Noise(z, var):
    return (randn() * var) + z


class Sensor:
    x_pos = 0
    x_vel = 0
    x_acc = 0

    S_Var = 0
 
    def __init__(self, x, dx, dxx, SV):
        self.x_pos = x
        
        self.x_vel = dx
        
        self.x_acc = dxx

        self.S_Var = SV

    def read(self, epoch):
        self.x_pos = self.x_pos + (epoch * self.x_vel) + (epoch**2 * self.x_acc)
        self.x_vel = self.x_vel + (epoch * self.x_acc)
        return Noise(self.x_pos, self.S_Var)

    
        
