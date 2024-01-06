import matplotlib.pyplot as plt


weights = [158.0, 164.2, 160.3, 159.9, 162.1, 164.6, 169.6, 167.4, 166.4, 171.0, 171.2, 172.6]
time_scale = 1.0
scale_factor = 4.0/10.0


def gh_filter(gain_rate=-1.0, estimate=160.0):
    estimates, predictions = [estimate], []
    for i in weights:
        prediction = estimate + gain_rate * time_scale
        estimate = prediction + ((i - prediction) * scale_factor)
        gain_rate = gain_rate + (((i - prediction) / time_scale) * 1/3)
        estimates.append(estimate)
        predictions.append(prediction)
    
    return estimates, predictions 

line1, line2 = g_filter()

plt.plot(weights, marker='o')
plt.plot(line1)
plt.plot(line2)
plt.show()

