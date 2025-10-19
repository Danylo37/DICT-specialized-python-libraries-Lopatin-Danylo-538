from os.path import join as p_join
import numpy as np


def task1():
    arr = np.load(p_join("files", "first.npy"))
    print("Shape:", arr.shape)
    print("Size:", arr.size)
    print(f"Array:\n{arr}")


def task2():
    students = np.loadtxt(p_join("files", "students.txt"), dtype=str)
    results = np.load(p_join("files", "results.npy"))

    n_students, n_classes = results.shape
    print(f"Number of students: {n_students}")
    print(f"Number of classes: {n_classes}")

    ratings = np.where(results == -1, 0, results).sum(axis=1)

    order_desc = np.argsort(ratings)[::-1]
    students_sorted = students[order_desc]
    ratings_sorted = ratings[order_desc]

    np.savetxt(p_join("files", "rating.txt"), np.column_stack((students_sorted, ratings_sorted)), fmt='%s %s')

    no_misses_mask = np.all(results != -1, axis=1)
    no_misses = students[no_misses_mask]
    print("\nНе пропустили жодного заняття:", no_misses)

    present = np.ma.masked_equal(results, -1)

    only_5_mask = np.ma.all(present == 5, axis=1).filled(False)
    only_5 = students[only_5_mask]
    print("Мають тільки відмінні оцінки (5):", only_5)

    only_4_5_mask = np.ma.all(np.logical_or(present == 4, present == 5), axis=1).filled(False)
    only_4_5 = students[only_4_5_mask]
    print("Мають відмінні та добрі оцінки (4 та 5):", only_4_5)

    never_attended_mask = np.all(results == -1, axis=1)
    never_attended = students[never_attended_mask]
    print("Не були на жодному занятті:", never_attended)


if __name__ == "__main__":
    tasks = [task1, task2]

    for num, task in enumerate(tasks, start=1):
        print(f'Task {num}:')
        task()
        print()