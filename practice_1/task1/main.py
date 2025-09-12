def task(numbers, d):
    for idx in range(len(numbers) - 1):
        if d >= numbers[idx] + numbers[idx + 1]:
            return idx

    return -1


def main():
    numbers = [0.5, 2.8, 9.1, -0.3, 10, -1, 2.1, 8.2]
    d = 1.5

    print("List:", numbers)

    print(f"\nTest #1 (with D: {d}):")
    print(task(numbers, d))

    d = 0

    print(f"\nTest #2 (with D: {d}):")
    print(task(numbers, d))


if __name__ == '__main__':
    main()
