import os.path


def task(m1_path, result_path):
    result = []

    with open(m1_path, 'r') as m1:
        for idx, line in enumerate(m1, start=1):
            line = line.split()
            line_set = set(line)

            if len(line) != len(line_set):
                result.append(str(idx))

    with open(result_path, 'w') as result_file:
        result_file.write(' '.join(result))


def main():
    matrix_path = os.path.join("files", "matrix")
    result_path = os.path.join("files", "result")

    task(matrix_path, result_path)


if __name__ == '__main__':
    main()
