import matplotlib.pyplot as plt
import numpy as np
data=np.random.normal(0,1,1000)
plt.hist(data, bins=30)
plt.xlabel('Random Normal Data')
plt.ylabel('Frequency')
plt.title('Histogram of Random Normal Data')
plt.show()