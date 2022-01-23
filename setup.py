import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="polynomial_regression_model",
    version="3.1.1",
    description="Python package that analyses the given datasets and comes up with the best regression representation with either the smallest polynomial degree possible, to be the most reliable without overfitting or other models such as exponentials and logarithms",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/nikolas-virionis/polynomial-regression",
    author="Nikolas B Virionis",
    author_email="nikolas.virionis@bandtec.com.br",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["polynomial_regression"],
    install_requires=["numpy", "matplotlib", "sklearn"],
)
