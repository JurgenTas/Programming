# coding=utf-8
__author__ = 'J Tas'

import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
from sklearn.cross_validation import train_test_split


def load():
    """
    1. CRIM      per capita crime rate by town
    2. ZN        proportion of residential land zoned for lots over 25,000 sq.ft.
    3. INDUS     proportion of non-retail business acres per town
    4. CHAS      Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
    5. NOX       nitric oxides concentration (parts per 10 million)
    6. RM        average number of rooms per dwelling
    7. AGE       proportion of owner-occupied units built prior to 1940
    8. DIS       weighted distances to five Boston employment centres
    9. RAD       index of accessibility to radial highways
    10. TAX      full-value property-tax rate per $10,000
    11. PTRATIO  pupil-teacher ratio by town
    12. B        1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town
    13. LSTAT    % lower status of the population
    14. MEDV     Median value of owner-occupied homes in $1000's
    """
    df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data', header=None,
                     sep='\s+')
    df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT',
                  'PRICE']
    train, test = train_test_split(df, test_size=0.2, random_state=1)

    x_train = train.ix[:, 'CRIM':'LSTAT']
    y_train = train.ix[:, 'PRICE']
    x_test = test.ix[:, 'CRIM':'LSTAT']
    y_test = test.ix[:, 'PRICE']
    return x_train, y_train, x_test, y_test


def fit(x_train, y_train, x_test, y_test):
    """
    Fit the model
    :param x_train: x-training data (dataframe)
    :param y_train: y-training data (dataframe)
    :param x_test:  x-test data (dataframe)
    :param y_test:  y-test data (dataframe)
    :return:
    """
    # Fit and summarize OLS model
    model = sm.OLS(y_train, x_train)
    res = model.fit()
    print(res.summary())

    # Calculate predictions
    y_train_pred = res.predict(x_train)
    y_test_pred = res.predict(x_test)

    # Residual plot
    plt.scatter(y_train_pred, y_train_pred - y_train, c='blue', marker='o', label='Training Data')
    plt.scatter(y_test_pred, y_test_pred - y_test, c='red', marker='s', label='Test Data')
    plt.show()


def main():
    x_train, y_train, x_test, y_test = load()
    fit(x_train, y_train, x_test, y_test)


if __name__ == "__main__":
    main()
