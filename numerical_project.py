import numpy as np

# Differential equation: dy/dx = f(x, y)
def f(x, y):
    return 3 * np.exp(2 * x) * y

# Second derivative for Taylor (manually derived)
def d2f(x, y):
    return 15 * np.exp(4 * x) * y

# Euler Method
def euler_method(f, x0, y0, h, n):
    x, y = x0, y0
    print("Euler Method:")
    for i in range(n + 1):
        print(f"x = {x:.2f}, y = {y:.6f}")
        y += h * f(x, y)
        x += h

# Taylor Method (2nd order)
def taylor_method(f, x0, y0, h, n):
    x, y = x0, y0
    print("\nTaylor Method (2nd Order):")
    for i in range(n + 1):
        print(f"x = {x:.2f}, y = {y:.6f}")
        y += h * f(x, y) + (h**2 / 2) * d2f(x, y)
        x += h

# Runge-Kutta 6th Order Method
def rk6_method(f, x0, y0, h, n):
    x, y = x0, y0
    print("\nRunge-Kutta 6th Order:")
    for i in range(n + 1):
        print(f"x = {x:.2f}, y = {y:.6f}")
        k1 = f(x, y)
        k2 = f(x + h/4, y + h/4 * k1)
        k3 = f(x + h/4, y + h/8 * k1 + h/8 * k2)
        k4 = f(x + h/2, y - h/2 * k2 + h * k3)
        k5 = f(x + 3*h/4, y + 3*h/16 * k1 + 9*h/16 * k4)
        k6 = f(x + h, y - 3*h/7 * k1 + 2*h/7 * k2 + 12*h/7 * k3 - 12*h/7 * k4 + 8*h/7 * k5)
        y += h * (7*k1 + 32*k3 + 12*k4 + 32*k5 + 7*k6) / 90
        x += h

# Initial conditions and parameters
x0 = 0
y0 = 1
h = 0.5
n = int((y0 - x0) / h)

# Run all methods
euler_method(f, x0, y0, h, n)
taylor_method(f, x0, y0, h, n)
rk6_method(f, x0, y0, h, n)
