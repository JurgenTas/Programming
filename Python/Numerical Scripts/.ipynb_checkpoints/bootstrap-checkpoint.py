import numpy.random as nr
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as st


def mad(arr):
    """ Median Absolute Deviation: a "Robust" version of standard deviation.
        Indices variabililty of the sample.
        https://en.wikipedia.org/wiki/Median_absolute_deviation 
    """
    arr = np.ma.array(arr).compressed(
    )  # should be faster to not use masked arrays.
    med = np.median(arr)
    return np.median(np.abs(arr - med))


nr.seed(123)
# dummy data
a, n = 2, 10000
data = nr.pareto(a, n)

# bootstrap loop
m = 10000
arr1, arr2 = [], []
for i in range(m):

    nr.seed(i)
    sample1 = nr.choice(data, size=n, replace=True)

    nr.seed(i)
    alpha = 4
    weights = nr.dirichlet(alpha=[alpha]*n)

    nr.seed(i)
    sample2 = nr.choice(data, size=n, p=weights, replace=True)

    arr1.append(mad(sample1))
    arr2.append(mad(sample2))


conf1 = st.t.interval(alpha=0.95,
                      df=len(arr1)-1,
                      loc=np.mean(arr1),
                      scale=st.sem(arr1))

conf2 = st.t.interval(alpha=0.95,
                      df=len(arr2)-1,
                      loc=np.mean(arr2),
                      scale=st.sem(arr2))

print(conf1)
print(conf2)

sns.histplot(arr1, color='r', bins=50)
sns.histplot(arr2, color='b', bins=50)
plt.show()
