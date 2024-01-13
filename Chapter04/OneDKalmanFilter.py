import matplotlib.pyplot as plt
from numpy.random import randn
import math

class dog:
    positions = []
    currentPosition = 0
    previousMove = 0
    jD = 1
    def __init__(self, n=[1, 1, 0, 0, 0, 0, 0, 0, 1, 0]):
        self.positions = n
    def move(self):
        if (randn() > 0):
            self.previousMove = self.jD
            self.currentPosition = (self.currentPosition + self.jD) % len(self.positions)
        else:
            self.previousMove = -self.jD
            self.currentPosition = (self.currentPosition - self.jD ) % len(self.positions)

    def getSensorReading(self):
        return self.positions[self.currentPosition], self.previousMove
    
    def getErrorSensorReading(self):
        randomVal = randn()
        if randomVal < -1.5:
            return self.positions[self.currentPosition -1], self.previousMove
        if randomVal > 1.5:
            return self.positions[self.currentPosition +1], self.previousMove
        return self.getSensorReading()



def plotDis(mean, stan):
    x = [mean + i/10. for i in range(-100, 100)]
    y = []
    for i in x:
        val = 2.713**((-(i - mean)**2)/(2*(stan**2))) /(stan* math.sqrt(2*3.14159))
        y.append(val)
    plt.plot(x, y)
    plt.show()

def predict(m1, v1, m2, v2):
    return (m1 + m2, v1 + v2)
    
def update(m1, v1, m2, v2):
    avgMean = ((m2 * v1) + (m1 * v2)) / (v1 + v2)
    avgVar  = (v1 * v2) / (v1 + v2)
    return (avgMean, avgVar)

Simon = dog()

for i in range(5):
    Simon.move()
    Simon.getSensorReading()



plotDis(10,1)

print(update(10., .2**2, 11., .1**2))
















