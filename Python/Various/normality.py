# Box-cox Transformation of non-normal data

# import modules
import numpy as np
from scipy import stats

# plotting modules
import seaborn as sns
import matplotlib.pyplot as plt


def bootstrap(data, n=1000, func=np.mean):
    """
    Generate `n` bootstrap samples, evaluating `func`
    at each resampling. `bootstrap` returns a function,
    which can be called to obtain confidence intervals
    of interest.
    """
    simulations = list()
    sample_size = len(data)
    for c in range(n):
        itersample = np.random.choice(data, size=sample_size, replace=True)
        simulations.append(func(itersample))
    simulations.sort()

    def ci(p, decimals=2):
        """
        Return 2-sided symmetric confidence interval specified
        by p
        """
        u_pval = (1 + p) / 2.0
        l_pval = 1 - u_pval
        l_indx = int(np.floor(n * l_pval))
        u_indx = int(np.floor(n * u_pval))
        return (
            round(simulations[l_indx], decimals),
            round(simulations[u_indx], decimals),
        )

    return ci


# generate log-normal data:
mu, sigma = 1.0, 0.5
original_data = 1e3 * np.random.lognormal(mu, sigma, 1000)

# transform training data & save lambda_val value:
_data, lambda_val = stats.boxcox(original_data)

# creating axes to draw plots:
fig, ax = plt.subplots(1, 2)

# plotting the original data(non-normal) and transformed data:
sns.histplot(original_data, label="Non-Normal", color="green", ax=ax[0], bins=25)
sns.histplot(_data, label="Normal", color="red", ax=ax[1], bins=25)

# adding legends to the subplots:
plt.legend(loc="upper right")

# rescaling the subplots:
fig.set_figheight(5)
fig.set_figwidth(10)

plt.savefig("plot.png")
print("Lambda used for Box-Cox : {:.4f}".format(lambda_val))

# test whether a sample differs from a normal distribution:
k2, p = stats.normaltest(_data)
alpha = 1e-3
print("p : {:.4f}".format(p))
if p < alpha:  # null hypothesis: fitted_data comes from a normal distribution
    print("The null hypothesis can be rejected")
else:
    print("The null hypothesis cannot be rejected")

# determine confidence intervals for mean:
boot = bootstrap(_data, n=5000)
print("CI for mu : ", [boot(i) for i in (0.95, 0.99)])

# determine confidence intervals for sigma:
boot = bootstrap(_data, n=5000, func=np.std)
print("CI for sigma : ", [boot(i) for i in (0.95, 0.99)])

# print distribution statistics:
print("mu : {:.2f}".format(np.mean(_data)))
print("sigma : {:.2f}".format(np.std(_data)))
print("skew : {:.4f}".format(stats.skew(_data)))
print("kurt : {:.4f}".format(stats.kurtosis(_data)))
