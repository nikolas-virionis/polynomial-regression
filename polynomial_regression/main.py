import numpy as np
from pylab import *
from sklearn.metrics import r2_score
import expon
import log
import sinusoidal
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")


class Regression:
    """The Class Regression tests if a set of data is fit in either a polynomial regression model, or others such as exponential or logarithmic and returns a variety of results regarding its calculations"""
    __list_return: list

    def __init__(self, x: list[number], y: list[number]):
        np.random.seed(2)
        if not len(x) == len(y):
            raise Exception("Invalid input for x or y")
        if not len(x) > 2 and len(y) > 2:
            raise Exception("Invalid input for x or y")
        self.__x = np.array(x)
        self.__y = np.array(y)
        self.__regression()
        if not self.__list_return[1]:
            self.__regression(control=True)

    @property
    def x(self) -> list[number]:
        """Returns the list given in the x axis"""
        return self.__x.tolist()

    @property
    def y(self) -> list[number]:
        """Returns the list given in the y axis"""
        return self.__y.tolist()

    def get_r2(self) -> float:
        """Returns coefficient of determination (r²)"""
        return self.__list_return[0]

    def not_polynomial_warn(self):
        return f"{'An exponential' if self.__list_return[5] == 'expon' else 'A logarithmic'  if self.__list_return[5] == 'logarithm' else 'A sinusoidal'} model does not have a degree, since the function would be somewhat like {'y = a * b^x + c' if self.__list_return[5] == 'expon' else 'y = a * log(b + x) + c'  if self.__list_return[5] == 'logarithm' else 'y = a * sin(b * (x - c)) + d'}"

    def get_degree(self) -> int:
        """Returns the polinomial degree of the regression"""
        return self.__list_return[1] if self.__list_return[5] == "polynomial" else self.not_polynomial_warn()

    def get_ordinal(self) -> str:
        """Returns the ordinal suffix of the regression degree"""
        return self.__list_return[2] if self.__list_return[5] == "polynomial" else self.not_polynomial_warn()

    def get_full_degree(self) -> str:
        """Returns the polinomial degree with the ordinal suffix of the regression"""
        return str(self.get_degree()) + str(self.get_ordinal()) if self.__list_return[5] == "polynomial" else self.not_polynomial_warn()

    def get_coefficients(self) -> list[float]:
        """Returns the list of coefficients of the regression equation, 
        going from the greater index degree towards the linear coefficient"""
        return self.__list_return[3]

    def get_prediction(self, x: float) -> float:
        """Returns the prediction for a specific x value using the polynomial regression calculated"""
        return self.__list_return[4](x)

    def equation_string(self) -> str:
        """Returns the polynomial equation as a string to be better displayed if necessary"""
        equation = "y = "
        equationX = ""
        coefficients = self.__list_return[3]
        if self.__list_return[5] == "polynomial":
            for i in range(len(coefficients) - 1, -1, -1):
                if round(coefficients[len(coefficients) - (i + 1)], 4) == 0:
                    continue
                equationX += f"{'' if i == len(coefficients) - 1 else '+' if coefficients[len(coefficients) - (i + 1)] > 0 else '-'} {str(abs(round(coefficients[len(coefficients) - (i + 1)], 4))) + (f'x^{i}' if i > 1 else 'x' if i > 0 else '')} "
        elif self.__list_return[5] == "expon":
            equationX = f"{f'{round(coefficients[0], 4)} * ' if round(coefficients[0], 4) != 1 else ''}{round(coefficients[1], 4)}^x"
        elif self.__list_return[5] == "logarithm":
            equationX = f"{f'{round(coefficients[0], 4)} * ' if round(coefficients[0], 4) != 1 else ''}log({round(coefficients[1], 4)} + x) {f'+ {round(coefficients[2], 4)}' if round(coefficients[2], 4) > 0 else '' if round(coefficients[2], 4) == 0 else f'- {abs(round(coefficients[2], 4))}'}"
        elif self.__list_return[5] == "sinusoidal":
            equationX = f"{f'{round(coefficients[0], 4)} * ' if round(coefficients[0], 4) != 1 else ''}sin({f'{round(coefficients[1], 4)} * ' if round(coefficients[1], 4) != 1 else ''} (x {f'- {np.radians(round(coefficients[2], 4))}' if round(coefficients[2], 4) > 0 else f'+ {round(np.radians(coefficients[2]), 4)}' if round(coefficients[2], 4) < 0 else ''})) {f'- {round(coefficients[3], 4)}' if round(coefficients[3], 4) < 0 else f'+ {round(coefficients[3], 4)}' if round(coefficients[3], 4) > 0 else ''}"
        equation += equationX
        return equation

    def __set_list_return(self, r2, degree, coefficients, prediction, type):
        self.__list_return = (
            r2,
            degree,
            "st" if degree == 1 else "nd" if degree == 2 else "rd" if degree == 3 else "th",
            coefficients,
            lambda x: prediction(x),
            type
        )

    def visualization(self):
        """
        Plots both a scatter plot of the data and a line of the regression calculated
        """
        xp = np.linspace(min(self.__x), max(self.__x),
                         (max(self.__x) - min(self.__x)) * 50)
        plt.scatter(self.__x, self.__y)
        plt.plot(xp, self.__list_return[4](xp), c='r')
        plt.show()

    def __regression(self, control=True):
        """Function thats calculates the best polynomial regression given the two datasets"""
        r2 = 0
        degree = 0
        predict = ""
        coefficient = []
        type = ""
        x = self.__x
        y = self.__y
        for i in range(-2, 31):
            category = ""
            coefficients = []
            prediction = lambda x: 0
            if i == -2:
                category = "expon"
                coefficients = expon.regression(self.__x, self.__y)

                prediction = lambda x: expon.prediction(
                    self.__x, self.__y, x)
            elif i == -1:
                category = "logarithm"
                coefficients = log.regression(self.__x, self.__y)

                prediction = lambda x: log.prediction(
                    self.__x, self.__y, x)
            elif i == 0:
                category = "sinusoidal"
                coefficients = sinusoidal.regression(self.__x, self.__y)
                prediction = lambda x: sinusoidal.prediction(
                    self.__x, self.__y, x)
            else:
                category = "polynomial"
                coefficients = np.polyfit(x, y, i)
                prediction = np.poly1d(coefficients)

            # if r2_score(y, prediction(x)) >= 0.999:
            #     r2 = r2_score(y, prediction(x))
            #     degree = i
            #     predict = prediction
            #     coefficient = coefficients
            #     type = category
            #     break

            if round(r2, 4) <= round(r2_score(y, prediction(x)), 4) - (i / 50 if control and i > 0 else 0):
                r2 = r2_score(y, prediction(x))
                degree = i
                predict = prediction
                coefficient = coefficients
                type = category

        self.__set_list_return(r2, degree, coefficient, predict, type)

    def best_regression_model(self) -> str:
        """Returns the best degree of polynomial formatted as a string"""
        return "\n " + f"The best polynomial to describe the given sets' behaviour is the {self.get_full_degree()} degree polynomial" if self.__list_return[5] == "polynomial" else "The best regression model to describe the given sets' behaviour is the exponential" if self.__list_return[5] == "expon" else "The best regression model to describe the given sets' behaviour is the logarithmic" if self.__list_return[5] == "logarithm" else "The best regression model to describe the given sets' behaviour is the sinusoidal"

    def coefficient_of_determination(self) -> str:
        """Returns the coefficient of determination (R²) formatted as a string"""
        return "\n " + f"It has a coefficient of determination of {self.get_r2():.4f}"

    def __r2_interpretation(self) -> str:
        """Returns the coefficient of determination interpretation if needed"""
        if self.get_r2() < 0.45:
            return "\n" + f"This index being low, represents it is not possible to find any reliably predictable behaviour given the previous datasets, therefore the actual accuracy for the predictions will be low and highly dependent on chance"
        if self.get_r2() < 0.6:
            return "\n" + f"This index represents the predictions will not have optimal accuracy when making predictions since the given datasets don't set up an ideal predictable behaviour"
        return ""

    def equation_text(self) -> str:
        """Returns the polinomial equation formatted as a string"""
        return "\n " + f"The equation can be written as {self.equation_string()}" + "\n and makes predictions via the get_prediction function\n"

    def full_text_analysis(self) -> str:
        """Returns the full text analysis"""
        return self.best_regression_model() + self.coefficient_of_determination() + self.__r2_interpretation() + self.equation_text()

    def full_analysis(self) -> str:
        """Returns the full analysis with all text and visualization"""
        self.visualization()
        return self.full_text_analysis()

    def print_full_analysis(self):
        """Prints the full analysis with all text and visualization"""
        print(self.full_text_analysis())
        self.visualization()


def regress(y: list[number], x: list[number] = None):
    """Returns an instance of the Regression Class"""
    if x is None:
        x = list(range(1, len(y) + 1))
    return Regression(x, y)
