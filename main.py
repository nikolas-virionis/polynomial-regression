import numpy as np
from pylab import *
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

np.random.seed(2)

# This script tries to find the best polynomial regression for two given sets of data

# submit both the lists to the variables below and exeute the whole script

x = np.random.normal(3.0, 1.0, 1000)
y = np.random.normal(50.0, 10.0, 1000) / x


def list_return(r2, degree, coefficients, prediction):
    return (
        r2,
        degree,
        "st" if degree == 1 else "nd" if degree == 2 else "rd" if degree == 3 else "th",
        coefficients,
        lambda x: prediction(x)
    )


def equation(coefficients):
    equation = "y = "
    equationX = ""
    for i in range(len(coefficients) - 1, -1, -1):
        if round(coefficients[len(coefficients) - (i + 1)], 4) == 0:
            continue
        equationX += f"{'+' if coefficients[len(coefficients) - (i + 1)] > 0 else '-'} {str(abs(round(coefficients[len(coefficients) - (i + 1)], 4))) + (f'x^{i}' if i > 1 else 'x' if i > 0 else '')} "

    equationX = equationX[2:]
    equation += equationX
    return equation


def polynomial(x, y, control=True):
    x = np.array(x)
    y = np.array(y)
    r2 = 0
    degree = 0
    predict = ""
    coefficient = []
    for i in range(1, 16):
        coefficients = np.polyfit(x, y, i)
        prediction = np.poly1d(coefficients)

        if r2_score(y, prediction(x)) - i >= 0.9:
            return list_return(r2_score(y, prediction(x)), i, coefficients, prediction)

        if r2 < r2_score(y, prediction(x)) - (i / 30 if control else 0):
            r2 = r2_score(y, prediction(x))
            degree = i
            predict = prediction
            coefficient = coefficients

    return list_return(r2, degree, coefficient, predict)


regression = polynomial(x, y)
r2, degree, ordinal, coefficients, predict = regression if regression[1] else polynomial(
    x, y, False)
if r2 > 0.1:
    print(f"\nThe best polynomial to describe the given sets' behaviour is the {str(degree) + ordinal} degree polynomial\n It has a coefficient of determination of {r2}\n{f' This index being low, represents it is not possible to find any reliably predictable behaviour given the previous datasets, therefore the actual accuracy for the predictions will be low and highly dependent on chance' if r2 < 0.45 else f''' This index represents the predictions will not have optimal accuracy when making predictions since the given datasets don't set up a good predictable behaviour''' if r2 < 0.6 else ''}\n The equation can be written as {equation(coefficients)}\n and makes predictions via the predict function\n")

    xp = np.linspace(min(x), max(x))
    plt.scatter(x, y)
    plt.plot(xp, predict(xp), c='r')
    plt.show()
else:
    print("The given datasets cannot correlate to each other in a predictable way what so ever, having that said any prediction, based on this past data, would be a blind guess, therefore no equation could be made")
