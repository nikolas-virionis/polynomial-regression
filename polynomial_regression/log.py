import numpy as np
from pylab import *
from scipy.optimize import curve_fit
import warnings
warnings.filterwarnings("ignore")


def function(x, a, b, c):
    """Function that represents the logarithmic equation"""
    return a * np.log10(b + x) + c


def regression(x, y):
    """Function that returns the regression equation coefficients"""
    try:
        popt, pcov = curve_fit(function, x, y, p0=[5, 3, 4])
    except Exception:
        return [0, 0, 0]
    return popt


def prediction(X, Y, x):
    """Function that returns the prediction made with the regressipon equation"""
    a, b, c = regression(X, Y)
    return function(x, a, b, c)
