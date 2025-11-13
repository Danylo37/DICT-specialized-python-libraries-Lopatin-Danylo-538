import numpy as np
from scipy.optimize import minimize
import time
import warnings


def f(x):
    return x[0]**2 + x[1]**2 + 4*x[0] + 6*x[1] + 13


def f_grad(x):
    return np.array([2*x[0] + 4, 2*x[1] + 6])


def f_hess(_x):
    return np.array([[2, 0], [0, 2]])


def f_max(x):
    return -f(x)


def f_max_grad(x):
    return -f_grad(x)


def f_max_hess(_x):
    return -f_hess(_x)


def constraint1(x):
    return -x[0]**2 - x[1]**2 + 8*x[0] + 6*x[1] - 4


def constraint1_grad(x):
    return np.array([-2*x[0] + 8, -2*x[1] + 6])


def constraint1_hess(_x):
    return np.array([[-2, 0], [0, -2]])


def constraint2(x):
    return 24 - 3*x[0] - 2*x[1]


def constraint2_grad(_x):
    return np.array([-3, -2])


def constraint2_hess(_x):
    return np.array([[0, 0], [0, 0]])


def constraint3(x):
    return 24 - 2*x[0] - 3*x[1]


def constraint3_grad(_x):
    return np.array([-2, -3])


def constraint3_hess(_x):
    return np.array([[0, 0], [0, 0]])


def optimize_and_print(func, func_grad, method, constraints, negate_result=False, func_hess=None):
    num_of_points = 10
    start_points = [np.random.uniform(-5, 5, 2) for _ in range(num_of_points)]
    best = None
    total_time = 0

    for x0 in start_points:
        with warnings.catch_warnings():
            warnings.filterwarnings('ignore', category=UserWarning)

            t0 = time.time()
            if method == 'trust-constr' and func_hess is not None:
                res = minimize(func, x0, method=method, jac=func_grad, hess=func_hess, constraints=constraints)
            else:
                res = minimize(func, x0, method=method, jac=func_grad, constraints=constraints)
            t1 = time.time()

        total_time += (t1 - t0)

        if res.success and (best is None or res.fun < best.fun):
            best = res

    avg_time = total_time * 1000 / num_of_points

    print(f"\n{method}:")
    print(f"x1 = {best.x[0]:.2f}, x2 = {best.x[1]:.2f}")
    result_value = -best.fun if negate_result else best.fun
    print(f"f(x) = {result_value:.2f}")
    print(f"Avg. time per iteration: {avg_time:.2f} ms")


def main():
    cons = [
        {'type': 'ineq', 'fun': constraint1, 'jac': constraint1_grad, 'hess': constraint1_hess},
        {'type': 'ineq', 'fun': constraint2, 'jac': constraint2_grad, 'hess': constraint2_hess},
        {'type': 'ineq', 'fun': constraint3, 'jac': constraint3_grad, 'hess': constraint3_hess}
    ]

    print("Min:")
    optimize_and_print(f, f_grad, 'trust-constr', cons, func_hess=f_hess)
    optimize_and_print(f, f_grad, 'SLSQP', cons)

    print("\nMax:")
    optimize_and_print(f_max, f_max_grad, 'trust-constr', cons, negate_result=True, func_hess=f_max_hess)
    optimize_and_print(f_max, f_max_grad, 'SLSQP', cons, negate_result=True)


if __name__ == "__main__":
    main()
