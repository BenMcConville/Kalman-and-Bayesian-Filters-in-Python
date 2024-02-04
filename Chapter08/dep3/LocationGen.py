from numpy.random import randn

def Noise(z, var):
    return (randn() * var) + z


class Sensor:
    x_pos = 0
    x_vel = 0
    x_acc = 0
    S1_Var = 0
    S2_Var = 0
 
    def __init__(self, x, dx, dxx, SV1, SV2):
        self.x_pos = x
        
        self.x_vel = dx
        
        self.x_acc = dxx

        self.S1_Var = SV1
        self.S2_Var = SV2

    def update(self, epoch):
        self.x_pos = self.x_pos + (epoch * self.x_vel) + (0.5 * epoch**2 * self.x_acc)
        self.x_vel = self.x_vel + (epoch * self.x_acc)

    def read1(self):
        return Noise(self.x_pos, self.S1_Var)

    def read2(self):
        return Noise(self.x_pos, self.S1_Var)

    
        
