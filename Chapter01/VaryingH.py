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

data =  [i / 50.0 for i in range(50)]
result01 = GHFilter(data, 1.0, 0.0, 0.0, 0.2, 0.05)
result02 = GHFilter(data, 1.0, 2.0, 0.0, 0.2, 0.05)
result03 = GHFilter(data, 1.0, 2.0, 0.0, 0.2, 0.5)

plt.plot(result01)
plt.plot(result02)
plt.plot(result03)
plt.plot(range(len(data)), data, 'o')
plt.legend(['dx = 0; H = 0.05', 'dx = 2; H = 0.05', 'dx = 2; H = 0.5', 'Data'])
plt.show()
