import numpy as np

class Problem:
    def __init__(self, c, b, A):
        self.c = c
        self.b = b
        self.A = A

    """
    Can be improved with the regex below, if I'm bored and I have too much free time
    (minimize|maximize) (([-+]?[0-9]+x[0-9]+)+)\n(subject to)\n((([-+]?[0-9]+x[0-9]+)+=[0-9]+[\n]?)+)
    """
    @staticmethod
    def from_file(path):
        c, b, A = [], [], []

        with open(path) as f:
            lines = f.readlines()
            c = [float(n) for n in lines[0].split(' ')]

            for index in range(1, len(lines)):
                split_line = lines[index].split(' ')
                row = [float(split_line[index]) for index in range(len(split_line) - 1)]
                
                b.append(float(split_line[-1]))
                A.append(row)

        return Problem(np.array([c]).T, np.array([b]).T, np.array(A))

    def __repr__(self):
        return f'===[c]===\n{str(self.c)}\n===[b]===\n{str(self.b)}\n===[A]===\n{str(self.A)}'

class Solution:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def to_file(self, path):
        with open(path, 'w') as f:
            f.write(f'x = {self.x.T[0]}\ny = {self.y.T[0]}')

    def __repr__(self):
        return f'===[x]===\n{str(self.x)}\n===[y]===\n{str(self.y)}'