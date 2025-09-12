import os.path


def task(m1_path, m2_path, result_path):
    result = []

    with (open(m1_path, 'r') as m1,
          open(m2_path, 'r') as m2):

        m1_arr = set(m1.read().split(sep=', '))
        m2_arr = set(m2.read().split(sep=', '))

        result = list(m1_arr & m2_arr)

    with open(result_path, 'w') as result_file:
        result_file.write(", ".join(result))


def main():
    m1_path = os.path.join("files", "M1")
    m2_path = os.path.join("files", "M2")
    result_path = os.path.join("files", "result")

    task(m1_path, m2_path, result_path)


if __name__ == '__main__':
    main()
