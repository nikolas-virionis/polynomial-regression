from pylab import *
from scipy.optimize import curve_fit
import warnings
warnings.filterwarnings("ignore")


def function(x, a, b):
    """Function that represents the exponential equation"""
    return a * (b ** x)


def regression(x, y):
    """Function that returns the regression equation coefficients"""
    try:
        popt, pcov = curve_fit(function, x, y, p0=[1, 0])
    except Exception:
        return [0, 0]
    return popt


def prediction(X, Y, x):
    """Function that returns the prediction made with the regressipon equation"""
    a, b = regression(X, Y)
    return function(x, a, b)
