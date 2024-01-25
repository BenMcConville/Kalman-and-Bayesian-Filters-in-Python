import matplotlib.pyplot as plt
from numpy.random import randn


def update(prior, measurement):
    x, P = prior
    z, R = measurement

    y = z - x        # Residual
    K = P / (R + P) # Kalman Gain

    x = x + K*y     # Posterior
    P = P * (1 - K)   # Posterior Var

    return (x, P)


def predict(posterior, movement):
    x, P  = posterior # mean and Var of Posterior
    dx, Q = movement  # mean and Var of Movement

    x = x + dx
    P = P + Q

    return (x, P)



def volt(voltage, std):
    return voltage + (randn() * std)


ideal_Voltage = 10

var = 0.13 ** 2


volt = [volt(ideal_Voltage, var) for i in range(50)]


P_Mean, P_Var = [], []
E_Mean, E_Var = [], []

low, upp = [], []


estimate, var = 10., 1.

for i in volt:
    estimate, var = predict((estimate, var), (0, 0.05 ** 2))
    P_Mean.append(estimate)
    P_Var.append(var)

    estimate, var = update((estimate, var), (i, .13**2))
    E_Mean.append(estimate)
    E_Var.append(var)
    low.append(estimate - var)
    upp.append(estimate + var)

plt.plot(volt, '*')
plt.plot(P_Mean, 'o')
plt.plot(E_Mean)

plt.fill_between(range(len(volt)), low, upp,facecolor='yellow', alpha=0.5)

plt.show()

print("Mean: " + str(estimate) + " Var: " + str(var))


plt.plot(E_Var)
plt.show()








