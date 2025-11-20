import numpy as np
from itertools import permutations
import random
import time

distances_dict = {
    (1, 2): 35, (1, 3): 352, (1, 4): 35, (1, 5): 224, (1, 6): 9, (1, 7): 720, (1, 8): 192, (1, 9): 61,
    (2, 3): 183, (2, 4): 63, (2, 5): 162, (2, 6): 8, (2, 7): 440, (2, 8): 282, (2, 9): 51,
    (3, 4): 454, (3, 5): 481, (3, 6): 248, (3, 7): 96, (3, 8): 899, (3, 9): 180,
    (4, 5): 100, (4, 6): 48, (4, 7): 770, (4, 8): 79, (4, 9): 172,
    (5, 6): 198, (5, 7): 615, (5, 8): 163, (5, 9): 394,
    (6, 7): 562, (6, 8): 246, (6, 9): 39,
    (7, 8): 1265, (7, 9): 521,
    (8, 9): 468
}

n_cities = 9
dist_matrix = np.full((n_cities, n_cities), np.inf)

for i in range(1, 10):
    dist_matrix[i-1, i-1] = 0

for (i, j), dist in distances_dict.items():
    dist_matrix[i-1, j-1] = dist
    dist_matrix[j-1, i-1] = dist

def calculate_path_length(path, matrix):
    total = 0
    for i in range(len(path)):
        total += matrix[path[i]-1, path[(i+1) % len(path)]-1]
    return total

def main():
    cities = list(range(2, 10))

    print("Method 1: Brute Force")
    best_path_bf = None
    best_distance_bf = float('inf')
    count_bf = 0

    start_time = time.time()
    for perm_tuple in permutations(cities):
        path = [1] + list(perm_tuple)
        distance = calculate_path_length(path, dist_matrix)
        count_bf += 1
        if distance < best_distance_bf:
            best_distance_bf = distance
            best_path_bf = path

    time_bf = time.time() - start_time

    print(f"Total permutations checked: {count_bf}")
    print(f"Best path: {best_path_bf}")
    print(f"Best distance: {best_distance_bf}")
    print(f"Time taken: {time_bf:.4f} seconds\n")

    print("Method 2: Random Permutation")
    best_path_random = None
    best_distance_random = float('inf')
    best_iteration = -1

    start_time = time.time()
    for iteration in range(count_bf):
        random_cities = cities.copy()
        random.shuffle(random_cities)
        path = [1] + random_cities
        distance = calculate_path_length(path, dist_matrix)
        if distance < best_distance_random:
            best_distance_random = distance
            best_path_random = path
            best_iteration = iteration

    time_random = time.time() - start_time

    print(f"Total random permutations generated: {count_bf}")
    print(f"Best iteration: {best_iteration}")
    print(f"Best path: {best_path_random}")
    print(f"Best distance: {best_distance_random}")
    print(f"Time taken: {time_random:.4f} seconds\n")

    print("Comparison and Conclusions:")
    print(f"Brute force optimal distance: {best_distance_bf}")
    print(f"Random method distance: {best_distance_random}")
    print(f"Brute force time: {time_bf:.4f} seconds")
    print(f"Random method time: {time_random:.4f} seconds")

if __name__ == "__main__":
    main()
