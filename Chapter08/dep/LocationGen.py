from numpy.random import randn

def Noise(z, var):
    return (randn() * var) + z


class Sensor:
    x_pos = 0
    y_pos = 0
    S_Var = 0
 
    def __init__(self, (x,y), SV):
        self.x_pos = x
        self.y_pos = y
        self.S_Var = SV

    def read(self):
        self.x_pos += 3.
        self.y_pos += 5.
        return (Noise(self.x_pos, self.S_Var), Noise(self.y_pos, self.S_Var))

    
        
