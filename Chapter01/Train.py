import matplotlib.pyplot as plt
from numpy.random import randn

dataPoints = 100

def getTrainData(dataPoints):
    velocity = 15.0
    position = 2300.0
    positions = []
    for i in range(dataPoints):
        positions.append(position + (velocity * i) + (randn() * 500))
    return positions


def GHFilter(data, timeStep=1.0, dx=1.0, x0=0.0, g=1.0, h=1.0):
    predictions, estimates = [], [x0]
    estimate = x0
    for x in data:
        prediction = estimate + (timeStep * dx)
        estimate   = prediction + ((x - prediction) * g)
        dx         = dx         + (((x - prediction) / timeStep) * h)

        estimates.append(estimate)
    
    return estimates

data = getTrainData(dataPoints) 
results01 = GHFilter(data, 1.0, 1.0, 2300.0, 0.25, 0.33)
results02 = GHFilter(data, 1.0, 1.0, 2300.0, 0.05, 0.01)

plt.plot(results01)
plt.plot(results02)
plt.plot(range(dataPoints), data, 'o')
plt.legend(['Filter01', 'Filter02', 'Data'])
plt.show()
