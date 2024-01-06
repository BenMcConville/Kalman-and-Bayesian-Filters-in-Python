import matplotlib.pyplot as plt
from numpy.random import randn

dataPoints = 100

def gen_data(x0, dx, count, noise_factor=1.0):
   return [x0 + (dx * i) + (randn() * noise_factor) for i in range(count)] 

def GHFilter(data, timeStep=1.0, dx=1.0, x0=0.0, g=1.0, h=1.0):
    predictions, estimates = [], [x0]
    estimate = x0
    for x in data:
        prediction = estimate + (timeStep * dx)
        estimate   = prediction + ((x - prediction) * g)
        dx         = dx         + (((x - prediction) / timeStep) * h)

        estimates.append(estimate)
    
    return estimates

#data = gen_data(0.0, 5.0, dataPoints, 50.0) # Here G=0.1 is the best
data =  range(10) + [10]*40                      # Here G=0.8 is the best
result01 = GHFilter(data, 1.0, 5.0, 0.0, 0.1, 0.01)
result02 = GHFilter(data, 1.0, 5.0, 0.0, 0.4, 0.01)
result03 = GHFilter(data, 1.0, 5.0, 0.0, 0.8, 0.01)

plt.plot(result01)
plt.plot(result02)
plt.plot(result03)
plt.plot(range(len(data)), data, 'o')
plt.legend(['G = 0.1', 'G = 0.4', 'G = 0.8', 'Data'])
plt.show()
