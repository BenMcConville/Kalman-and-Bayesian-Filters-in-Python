import matplotlib.pyplot as plt
from numpy.random import randn
class dog:
    positions = []
    currentPosition = 0

    def __init__(self, n=[1, 1, 0, 0, 0, 0, 0, 0, 1, 0]):
        self.positions = n
    def move(self):
        if (randn() > 0):
            self.currentPosition = (self.currentPosition + 1 ) % len(self.positions)
        else:
            self.currentPosition = (self.currentPosition - 1 ) % len(self.positions)
    def getSensorReading(self):
        return self.positions[self.currentPosition]

class BayesianFilter:
    belief = [] # This is the prior as we have not added the measurement (Like prediction)
    
    def __init__(self, n=10):
        self.belief = [1.0/n]*n
    
    def update(self, hall, sensorVal, percent):
        # Posterior = Normalised(Likelihood * Belief)        

        scale = percent / (1 - percent)
        likelihood = [1] * len(hall)
        for index, i in enumerate(hall): # Compute the likelihood of the measurement (Not Normalised)
            if (i == sensorVal):
                likelihood[index] *= scale
        
        for i in range(len(self.belief)): # Merge Likelihood and belief
            self.belief[i] *= likelihood[i]
        
        self.normalize() # This result is the posterior as it now includes the measurement (Estimate)

    def normalize(self):
        self.belief = [i / sum(self.belief) for i in self.belief]

    def shift(self, moves):
        newBelief = [1] * (len(self.belief) - 1)
        for i in range(len(self.belief)):    
            newBelief[i] = self.belief[(i + moves) % (len(self.belief) - 1)]
        self.belief = newBelief
   
 
Simon = dog()
BayF  = BayesianFilter(10)

# Our Belief in Simons Position
BayF.update(Simon.positions, Simon.currentPosition, 0)
plt.bar(range(len(BayF.belief)), BayF.belief)
plt.show()

#Simon.move()
#BayF.update(Simon.positions, Simon.currentPosition, 0)
BayF.shift(4)
plt.bar(range(len(BayF.belief)), BayF.belief)
plt.show()









