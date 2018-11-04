__author__ = 'Michael'


def read_lines(path):
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            yield line
