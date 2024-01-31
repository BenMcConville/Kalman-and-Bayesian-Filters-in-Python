import matplotlib.pyplot as plt
from numpy.random import randn
import math

# In the future, only linear Correlation will be considered


def var(numbers):
    avg = sum(numbers)/len(numbers)
    std = 0.
    for i in numbers:
        std = std + ((i - avg)**2)
    std = std / len(numbers)
    return std 

def cov(a, b):
    avg_a = sum(a) / len(a)
    avg_b = sum(b) / len(b)
    matrix = []
    line = []
    line.append(var(a))
    std = 0.
    for i in range(len(a)):
        std = std + ((a[i] - avg_a)*(b[i] - avg_b))
    std = std / len(a)
    line.append(std)
    matrix.append(line)
    
    matrix.append([line[1], line[0]])
    return matrix

height = [60, 62, 63, 65, 65.1, 68, 69, 70, 72, 74]
weight = [95, 120, 127, 119, 151, 143, 173, 171, 180, 210]

#plt.plot(height, weight, 'o')
plt.xlabel("Height")
plt.ylabel("Weight")
plt.show()

print("Variance Height: " + str(var(height)))
print("Covariance Height/Weight "+ str(cov(height, weight)))
