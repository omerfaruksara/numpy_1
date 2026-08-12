# Numerical Analysis Tools

This repository contains Python implementations of fundamental numerical analysis algorithms for solving complex mathematical problems. 

## Features

### 1. Root Finding Algorithms
Algorithms designed to find the roots of mathematical functions:
* **Bisection Method:** A robust, bracket-based root-finding algorithm.
* **Newton-Raphson Method:** A fast, derivative-based root-finding algorithm.
* **Numerical Differentiation:** Calculates derivatives dynamically, eliminating the need for hardcoded analytical derivatives.

### 2. Linear Equation Systems
Algorithms designed to solve systems of linear equations:
* **Gaussian Elimination:** Solves `Ax = b` systems using forward elimination and back substitution.
* **Partial Pivoting:** Minimizes rounding errors and prevents zero-division crashes by swapping rows based on maximum absolute values.
* **Singularity Checks:** Automatically detects singular matrices to avoid infinite calculations.

## Usage
To test all the algorithms, simply run the main execution script from your terminal:

```bash
python main.py