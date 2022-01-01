import numpy as np
from pylab import *
from scipy.optimize import curve_fit
import warnings
warnings.filterwarnings("ignore")


def function(x, a, b, c, d):
    """Function that represents the sinusoidal equation"""
    return a * np.sin(b * (x - c))+d


def regression(x, y):
    """Function that returns the regression equation coefficients"""
    popt, pcov = curve_fit(function, x, y, maxfev=99999999)

    return popt


def prediction(X, Y, x):
    """Function that returns the prediction made with the regressipon equation"""
    a, b, c, d = regression(X, Y)
    return function(x, a, b, c, d)
