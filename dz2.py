import numpy as np
import matplotlib.pyplot as plt

random_array_x = np.random.rand(5)
random_array_y = np.random.rand(5)

plt.scatter(random_array_x, random_array_y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Random Scatter Plot')
plt.grid()
plt.show()