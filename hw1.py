import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(0, 1, 1000)

plt.hist(x, 50)
plt.xlabel('Normally distributed random variable')
plt.ylabel('Frequency')
plt.title('Histogram of normal distribution')

plt.show()