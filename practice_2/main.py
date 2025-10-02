import numpy as np


def task1():
    arr = np.array([1, 2, 0, 0, 4, 0])
    indices_nonzero = np.nonzero(arr)[0]
    print(indices_nonzero)


def task2():
    matrix = np.arange(100).reshape(10, 10)
    print(f"Matrix:\n{matrix}")

    row_mins = matrix.min(axis=1)
    sum_row_mins = row_mins.sum()
    print(f"\nSum of row mins: {sum_row_mins}")

    col_maxs = matrix.max(axis=0)
    prod_col_maxs = col_maxs.prod()
    print(f"Product of column maxs: {prod_col_maxs}")


def task3():
    matrix = np.zeros((10, 10), int)

    matrix[0, :] = 1
    matrix[-1, :] = 1
    matrix[:, 0] = 1
    matrix[:, -1] = 1

    print(matrix)


def task4():
    matrix = np.diag([1, 2, 3, 4], k=-1)
    print(matrix)


def task5():
    chess = np.indices((8, 8)).sum(axis=0) % 2
    print(chess)


if __name__ == '__main__':
    tasks = [task1, task2, task3, task4, task5]

    for num, task in enumerate(tasks, start=1):
        print(f'Task {num}:')
        task()
        print()
