# Polynomial Regression

Python package that analyses the given datasets and comes up with the best regression representation with either the smallest polynomial degree possible, to be the most reliable without overfitting or other models such as exponentials and logarithms

<img alt="python logo" src="https://miro.medium.com/max/1400/1*-1ttHqMEzjjXduNdtIBKjQ.png" width = "45%">

- [Setup](#setup)
- [Methods](#methods)
- [Possible returns](#results)

## Setup 

### Requirements:
  - Python installed<br>
 The ideal version, to run the package is 3.9.x, the version in which the package was built over,<br> however,
 older versions of python 3 shouldn't have any issues, as the package does not use any <br> 
 fancy, new methods, not supported by older versions of Python 3.x
 
  - Installing the package<br>

For Microsoft Windows
~~~powershell
pip install polynomial-regression-model
~~~
For Linux
~~~bash
pip3 install polynomial-regression-model
~~~
  - Importing the package<br>

Firstly, it's necessary to import the method regress from the package polinomial_regression.main. It will analyse the parameter(s) and return the right object with all the methods it provides:
 ~~~ python
 from polinomial_regression.main import regress
 ~~~
 
 Then, there are two ways of using this model: One which provides both the axis values, x and y, and the math is done, and the other which provides only the y axis, would be more fitting to a use case of overtime monitoring of a single metric, select the best option to use below:

<strong> - Just as a quick note: the more data points provided, the more accurate the chosen regression model and it's equation are</strong>

 First the one that relates two different metrics, it is necessary to pass two same sized lists of numbers
 ~~~ python
 regression = regress([2, 4, 6, 8, 10], [1, 2, 3, 4, 5])
 # for it not to be reversed, the parameter 
 # order should be y, x
 ~~~

 And also the one that monitors the overtime behaviour of a single metric, it is necessary to pass a number list
 ~~~ python
 regression = regress([1, 2, 3, 4, 5, 2, 4, 6, 8, 10])
 ~~~

 
 After we already got our object instance, all there is left to do is enjoy the beauty of math
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
# E.g. [2, 3, 4, 5, 6] in case of the equation being 
# y = 2x^4 + 3x³ + 4x² + 5x + 6
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
 - best_regression_model
~~~python
regression.best_regression_model()
# returns the degree of the best fitting polynomial
# if the best model is a polynomial or else the best fitting 
# mathematical model inside a string to be displayed
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
regression.full_analysis()
# returns the full text analysis after plotting the
# visualization plots
~~~
 - print_full_analysis
~~~python
regression.print_full_analysis()
# prints the full text analysis and plots the
# visualization charts
~~~
### Correlation
- correlation
~~~ python
 regression.correlation()
 # returns the correlation between the datasets 
~~~ 
- correlation_way
~~~ python
 regression.correlation_way()
 # returns the way the two datasets are correlated 
 # to each other
~~~ 
- correlation_intensity
~~~ python
 regression.correlation_intensity()
 # returns the intensity by which the two datasets 
 # are correlated to each other
~~~ 
- correlation_interpretation
~~~ python
 regression.correlation_interpretation()
 # returns the interpretation of the correlation index
 # between the datasets 
~~~ 

## Results 
This package will return the best fitting model, trying its best to prevent overfitting, though it's good to clear out the possible outcomes:

- Polynomials:
The package was created to, at first, only analyse polynomial regression, and it still does, now from possible indexes 1 to 30, may not seem much but a 30 degree polynomial, unless really needed, may establish chaos, since it can kinda curve around to get all data points, but predictions may be as unreliable as it gets, despite the high r² score

- Exponentials:
Although polynomials are quite versatile and can describe a lot of patterns, others, more specific, such as exponentials, can sometimes, due to luck, be perfectly described by some polynomial, but still, to get the most out of it, the specificity is needed

- Logarithms:
Just like exponentials, it can sometimes be described by some crazy polynomials, though it loses accuracy quickly

- Sinusoidal:
Unlike the previously mentioned, a senoide is not so easy to represent, consistently, bt polynomials, it always fits perfect to the data that you test the model with but then predictions go 100% wrong, then this specificity is more than necessary

- Logistic:
Similarly to the previous, a logistic curve is not so easily represented by a polynomial and needs to have its own regression model in order to be better represented and be more reliable for predictions
