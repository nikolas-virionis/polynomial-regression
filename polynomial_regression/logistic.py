import numpy as np
from pylab import *
from scipy.optimize import curve_fit
import warnings
warnings.filterwarnings("ignore")


def function(x, L, c, k):
    return L / (1 + c * np.exp(-k * x))

def logifunc(x,L,x0,k,off):
    return L / (1 + np.exp(-k*(x-x0)))+off

def regression(x, y):
    """Function that returns the regression equation coefficients"""
    try:
        popt, pcov = curve_fit(function, x, y, p0=[200, 1, 1])
    except Exception:
        return [0, 0, 0]
    return popt


def prediction(X, Y, x):
    """Function that returns the prediction made with the regressipon equation"""
    L, c, k = regression(X, Y)
    return function(x, L, c, k)
