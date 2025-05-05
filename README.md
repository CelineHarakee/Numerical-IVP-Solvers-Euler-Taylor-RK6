# Numerical-IVP-Solvers-Python

This project demonstrates and compares three numerical methods for solving an Initial Value Problem (IVP) of the form: </br>
y' = 3e^{2x}y, y(0) = 1


We implemented and evaluated the following methods:
- Euler Method
- Taylor Method (2nd Order)
- Runge-Kutta Method (6th Order)

## Objective

To numerically solve the IVP and analyze the accuracy and behavior of each method compared to the exact solution. The project includes Python code, theoretical background, and a full report with visualizations.

---

## Methods Overview
- **Euler Method**: First-order, simple but low accuracy. Accumulates error quickly.
- **Taylor Method (2nd Order)**: More accurate by using second derivative.
- **Runge-Kutta 6th Order**: High accuracy using multiple slope evaluations.

---

## Numerical Example

- IVP: y' = 3e^{2x}y, y(0) = 1 
- Interval: x[0, 2] 
- Step size: h = 0.5

---

## Results
Plots compare the numerical solutions to the exact solution. The Runge-Kutta 6th order method produced results nearly identical to the true solution, while Euler and Taylor methods diverged for large x.



