import numpy as np


def task1():
    target = int(input("Enter an integer: "))
    array = np.random.randint(1, 100, 10)

    result = np.abs(array - target).argmin()
    print("Array:", array)
    print(f"Index of closest element to {target}: {result}, value: {array[result]}")


def task2():
    i = int(input("Enter an integer between 0 and 4: "))

    array = np.random.randint(1, 10, (5, 5))
    print(f"Initial array:\n{array}\n")

    array[:] = array[array[:, i].argsort()]
    print(f"Array sorted by column {i}:\n{array}")


def task3():
    v = np.array([1, 2, 3, 4, 5])
    k = 3
    zeros_count = (v.size - 1) * k

    v_with_zeros = np.zeros(v.size + zeros_count, int)
    v_with_zeros[::k + 1] = v

    print(v_with_zeros)


def task4():
    i, j = map(int, input("Enter two integers between 0 and 4 separated by space: ").split())

    matrix = np.random.randint(1, 10, (5, 5))
    print(f"Initial matrix:\n{matrix}\n")

    matrix[[i, j]] = matrix[[j, i]]
    print(f"Matrix after swapping rows {i} and {j}:\n{matrix}")



if __name__ == '__main__':
    np.random.seed(42)
    tasks = [task1, task2, task3, task4]

    for num, task in enumerate(tasks, start=1):
        print(f'Task {num}:')
        task()
        print()
