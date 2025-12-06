import numpy as np
from scipy.optimize import minimize
from shapely.geometry import Polygon
import matplotlib.pyplot as plt
import os


def get_rect(x, y, w, h):
    return Polygon([(x, y), (x + w, y), (x + w, y + h), (x, y + h)])


def objective(x, rects, region):
    n = len(x) // 2
    res = get_rect(x[0], x[1], rects[0][0], rects[0][1])
    for i in range(1, n):
        obj = get_rect(x[i*2], x[i*2+1], rects[i][0], rects[i][1])
        res = res.union(obj)
    return -region.intersection(res).area


def plot_rectangles(ax, region, coords, rects, title, W, H):
    n = len(rects)
    ax.add_patch(plt.Polygon(list(region.exterior.coords), fill=False, edgecolor='black', linewidth=2))
    colors = plt.cm.tab10(np.linspace(0, 1, n))

    res = get_rect(coords[0], coords[1], rects[0][0], rects[0][1])
    for i in range(1, n):
        obj = get_rect(coords[i*2], coords[i*2+1], rects[i][0], rects[i][1])
        res = res.union(obj)
    coverage_area = region.intersection(res).area

    for i in range(n):
        rect = get_rect(coords[i*2], coords[i*2+1], rects[i][0], rects[i][1])
        ax.add_patch(plt.Polygon(list(rect.exterior.coords), alpha=0.5, facecolor=colors[i], edgecolor='black'))
    ax.set_xlim(-1, W+1)
    ax.set_ylim(-1, H+1)
    ax.set_aspect('equal')
    ax.set_title(f'{title}\nCoverage Area: {coverage_area:.2f}')
    ax.grid(True)


def main():
    W, H = np.loadtxt(os.path.join('files', 'input.txt'), dtype=int, max_rows=1)
    n = int(np.loadtxt(os.path.join('files', 'input.txt'), dtype=int, skiprows=1, max_rows=1))
    rects_data = np.loadtxt(os.path.join('files', 'input.txt'), dtype=int, skiprows=2)
    rects = [tuple(rects_data[i]) for i in range(n)]

    region = Polygon([(0, 0), (W, 0), (W, H), (0, H)])

    x = np.zeros(2 * n)

    bounds = [(0, W), (0, H)] * n

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    plot_rectangles(ax1, region, x, rects, 'Initial Position', W, H)

    r = minimize(objective, x, args=(rects, region), bounds=bounds, method='L-BFGS-B')

    plot_rectangles(ax2, region, r.x, rects, 'Final Position', W, H)

    plt.tight_layout()
    plt.show()

    print("Final rectangle positions:")
    for i in range(n):
        print(f"Rectangle {i+1}: ({r.x[i*2]:.2f}, {r.x[i*2+1]:.2f})")


if __name__ == "__main__":
    main()
