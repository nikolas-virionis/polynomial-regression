import numpy as np
from pylab import *
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import warnings
warnings.filterwarnings("ignore")


def function(x, a, b, c):
    return a * (b ** x) + c


def regression(x, y):
    try:
        popt, pcov = curve_fit(function, x, y, p0=[1, 1e-6, 1])
    except Exception:
        return [0, 0, 0]
    return popt


def prediction(X, Y, x):
    a, b, c = regression(X, Y)
    return a * (b ** x) + c
