import numpy as np
from scipy.optimize import minimize, linprog


def f(x):
    return x[0]**2 + x[1]**2 - 2*x[0] - 6*x[1] + 13


def grad(x):
    return np.array([2*x[0] - 2, 2*x[1] - 6])


def task1():
    x0 = np.array([0.0, 0.0])

    res = minimize(f, x0, method='BFGS', jac=grad)
    print("Minimize (BFGS):", res.x, "\nMin. f =", res.fun)


def task2():
    consumption = np.array([[1.0, 2.0],
                            [2.0, 1.0],
                            [1.0, 0.8]])
    resources = np.array([6.0, 8.0, 5.0])
    prices = np.array([3.0, 2.0])

    A_ub = np.vstack([consumption, [1.0, -1.0], [0.0, 1.0]])
    b_ub = np.hstack([resources, [-1.0, 2.0]])

    res = linprog(c=-prices, A_ub=A_ub, b_ub=b_ub, bounds=[(0, None), (0, None)], method='highs')

    print(f"P1: {res.x[0]}\nP2: {res.x[1]}\nRevenue: {prices @ res.x}")


if __name__ == "__main__":
    tasks = [task1, task2]

    for num, task in enumerate(tasks, start=1):
        print(f'Task {num}:')
        task()
        print()