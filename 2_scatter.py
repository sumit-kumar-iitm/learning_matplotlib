import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('data/group5_train.txt', header=None, sep=' ', dtype=np.float32)

plt.scatter(data[0], data[1])

plt.show()
