import numpy as np
from pylab import *
from scipy.optimize import curve_fit
import warnings
warnings.filterwarnings("ignore")


def function(x, a, b, c):
    return a * np.log10(b + x) + c


def regression(x, y):
    try:
        popt, pcov = curve_fit(function, x, y)
    except Exception:
        return [0, 0, 0]
    return popt


def prediction(X, Y, x):
    a, b, c = regression(X, Y)
    return function(x, a, b, c)
