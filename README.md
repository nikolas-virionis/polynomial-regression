# Polynomial Regression

Python package that analyses the given datasets and comes up with the best polynomial regression representation with the smallest polynomial degree possible, to be the most reliable with the least complexity possible

<img alt="python logo" src="https://miro.medium.com/max/1400/1*-1ttHqMEzjjXduNdtIBKjQ.png" width = "45%">

- [Setup](#setup)
- [Methods](#methods)

## Setup 

### Requirements:
  - Python installed<br>
 The ideal version, to run the package is 3.9.x, the version in which the package was built over,<br> however,
 older versions of python 3 shouldn't have any issues, as the package does not use any <br> 
 fancy, new methods, not supported by older versions of Python 3.x
 
  - Installing the package<br>

For Microsoft Windows
~~~powershell
pip install polinomial_regression_model
~~~
For Linux
~~~bash
pip3 install polinomial_regression_model
~~~
  - Importing the package and getting the Class instance<br>

Firstly, there are two ways to import and use the package properly, though the difference is negligible:<br>
It is important to notice that either way its necessary to pass two same sized lists,
The first way is to import the Class Regression used for all the background processing itself, <br>
and instantiate it like in the example below:
 ~~~ python
 from polinomial_regression import Regression
 regression = Regression([1, 2, 3, 4, 5], [2, 4, 6, 8, 10])
 ~~~
 
Or else, alternatively, its possible to use a function which returns the instance of the Class<br> 
like in the example below:
 ~~~ python
 from polinomial_regression import regress
 regression = regress([1, 2, 3, 4, 5], [2, 4, 6, 8, 10])
 ~~~
Again, which one to choose is totally up to you, and it doesn't change any results what so ever, <br>
it's down to personal preference

## Methods
 - get_degree
~~~python
regression.get_degree()
# returns the polynomial degree(index) of the best fitting function
# E.g. 4 in the case of the equation being a 4th degree polynomial
~~~
 - get_ordinal
~~~python
regression.get_ordinal()
# returns the polynomial degree ordinal suffix (for mere better display)
# E.g. th in the case of the equation being a 4"th" degree polynomial
~~~
 - get_full_degree
~~~python
regression.get_full_degree()
# returns the polynomial degree(index) of the best fitting function 
# with its ordinal suffix
# E.g. 4th in the case of the equation being a "4th" degree polynomial
~~~
 - get_coefficients
~~~python
regression.get_coefficients()
# returns a list of all the coefficients of the polynomial equation
# E.g. [2, 3, 4, 5, 6] in case of the equation being y = 2x^4 + 3x³ + 4x² + 5x + 6
~~~
 - get_r2
~~~python
regression.get_r2()
# returns the coefficient of determination(R²) to find
# the accuracy of the best fitting regression just calculated
# E.g. 0.9 in the case of the equation being highly accurate]
# in relation to the test data
# I.e. although the perfect index would be 1, in real life data
# that is highly unlikely to happen
~~~
 - get_prediction
~~~python
regression.get_prediction(x: float)
# returns the prediction of the y value correspondent to 
# the x value informed according to the regression calculated
# E.g. 794 in the case of the equation being y = 2x^4 + 3x³ + 4x² + 5x + 6 
# (like the example above)
~~~
 - equation_string
~~~python
regression.equation_string()
# returns the polynomial equation calculated as a string 
# to be better displayed if necessary
# E.g. y = 2x^4 + 3x³ + 4x² + 5x + 6 in the case of the example above
~~~
 - visualization
~~~python
regression.visualization()
# returns the a graphic plot of both a scatter plot of the 
# real data and a line representing the regression calculated
~~~
 - best_degree_polynomial
~~~python
regression.best_degree_polynomial()
# returns the degree of the best fitting polynomial
# inside a string to be displayed
~~~
 - coefficient_of_determination
~~~python
regression.coefficient_of_determination()
# returns the coefficient of determination(R²) of the best 
# fitting polynomial inside a string to be displayed
~~~
 - equation_text
~~~python
regression.equation_text()
# returns the best fitting polynomial inside a string 
# to be displayed
~~~
 - get_prediction
~~~python
regression.get_prediction()
# returns the prediction of the y value correspondent to 
# the x value informed according to the regression calculated
# E.g. 794 in the case of the equation being y = 2x^4 + 3x³ + 4x² + 5x + 6 
# (like the example above)
~~~
 - full_text_analysis
~~~python
regression.full_text_analysis()
# returns the combination of the previous analysis, building 
# the full analysis as a text
~~~~~~
 - full_analysis
~~~python
regression.full_text_analysis()
# returns the full text analysis after plotting the
# visualization plots
~~~
 - print_full_analysis
~~~python
regression.full_text_analysis()
# prints the full text analysis and plots the
# visualization charts
~~~
