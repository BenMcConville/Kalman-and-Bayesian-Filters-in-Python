import matplotlib.pyplot as plt
from numpy.random import randn

'''
One Pro of the Discreate BayFilter is that you do not need to code the state transfer function and how it evolves from state to state.
To allow this to happen, we record the movement in the below example that is the vector of the dogs movement. So to avoid taking measurements and predicting how the system evolves we just ask how the system moves/evolves.
'''


class dog:
    positions = []
    currentPosition = 0
    previousMove = 0
    jD = 2
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

class BayesianFilter:
    belief = [] # This is the prior as we have not added the measurement (Like prediction)
    
    def __init__(self, n=10):
        self.belief = [1.0/n]*n
    
    def update(self, hall, sensorVal, n, z_val):
        # Posterior = Normalised(Likelihood * Belief)        
        #self.shift(n * -1)
        self.shiftPredict(n, 0.8, .1, .1) # Prediction Step : Everything after is the update step

        scale = z_val / (1.0000001 - z_val) 
        likelihood = [1] * len(hall)
        for index, i in enumerate(hall): # Compute the likelihood of the measurement (Not Normalised)
            if (i == sensorVal):
                likelihood[index] *= scale

        for i in range(len(self.belief)): # Merge Likelihood and belief
            self.belief[i] *= likelihood[i]
        
        self.normalize() # This result is the posterior as it now includes the measurement (Estimate)

    def normalize(self):
        self.belief = [i / sum(self.belief) for i in self.belief]

    def shift(self, n):
        self.belief = self.belief[n:] + self.belief[:n] 
    
    def shiftPredict(self, move, p_correct, p_over, p_under):
        n = len(self.belief)
        prior = [0]*n
        for i in range(n):
            prior[i] += self.belief[(i-move) % n]   * p_correct
            prior[i] += self.belief[(i-move+1) % n] * p_over
            prior[i] += self.belief[(i-move-1) % n] * p_under
        self.belief = prior
 
Simon = dog()
BayF  = BayesianFilter(10)





for i in range(10):
    Simon.move()
    #hallPosition, direction = Simon.getErrorSensorReading()
    hallPosition, direction = Simon.getSensorReading()
    BayF.update(Simon.positions, hallPosition, direction, 1)
    print(Simon.currentPosition)
    plt.bar(range(len(BayF.belief)), BayF.belief)
    plt.xlim(0, 10)
    plt.show()








