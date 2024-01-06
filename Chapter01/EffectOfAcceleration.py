import matplotlib.pyplot as plt
from numpy.random import randn

'''
The error created by the lagging of the linear filter on non Linear data is called Lag/Systemic error.
This is a fundamental property of GH Filters.
'''

dataPoints   = 10
start        = 5.0
rateOfChange = 2.0

def gen_data(x0, dx, dxx, count, noise_factor=1.0):
   return [x0 + ((dx + (dxx * i)) * i) + (randn() * noise_factor) for i in range(count)] 

def GHFilter(data, timeStep=1.0, dx=1.0, x0=0.0, g=1.0, h=1.0):
    predictions, estimates = [], [x0]
    estimate = x0
    for x in data:
        prediction = estimate + (timeStep * dx)
        estimate   = prediction + ((x - prediction) * g)
        dx         = dx         + (((x - prediction) / timeStep) * h)

        estimates.append(estimate)
    
    return estimates

data = gen_data(start, rateOfChange, 2.0, dataPoints, 0) 
results = GHFilter(data, 1.0, rateOfChange, start, 0.2, 0.02)

plt.plot(results)
plt.plot(range(dataPoints), data, 'o')
plt.legend(['Estimates', 'Data'])
plt.show()
