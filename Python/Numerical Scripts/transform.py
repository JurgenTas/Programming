import numpy as np
from sklearn.preprocessing import PowerTransformer
import matplotlib.pyplot as plt
import seaborn as sns

from matplotlib import style


# generate exponential data sample
data = np.random.exponential(scale=1, size=1000)
# histogram of the raw data with a skew
sns.histplot(data, kde=True, bins=25)
plt.show()
# reshape data to have rows and columns
data = data.reshape((len(data), 1))
# power transform the raw data
power = PowerTransformer(method='yeo-johnson', standardize=True)
data_trans = power.fit_transform(data)
# histogram of the transformed data
sns.histplot(data_trans, kde=True, bins=25)
plt.show()

# generate lognormal data sample
mu, sigma = 5., 1.  # mean and standard deviation
data = np.random.lognormal(mu, sigma, 1000)
# histogram of the raw data with a skew
sns.histplot(data, kde=True, bins=25)
plt.show()
# reshape data to have rows and columns
data = data.reshape((len(data), 1))
# power transform the raw data
power = PowerTransformer(method='yeo-johnson', standardize=True)
data_trans = power.fit_transform(data)
# histogram of the transformed data
sns.histplot(data_trans, kde=True, bins=25)
plt.show()
