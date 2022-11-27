from algorithm import PrimalDualInteriorPoint
from definitions import Problem, Solution

problems = [
    Problem.from_file('./input/course_example.txt'),
    Problem.from_file('./input/problem1.txt'),
    Problem.from_file('./input/problem2.txt')
]

if __name__ == '__main__':
    solver = PrimalDualInteriorPoint()

    for index, problem in enumerate(problems):
        solution = solver.fit(problem, 1000, 5, 100)

        solution.to_file(f'./output/solution{index + 1}.txt')
        print(f'Problem {index + 1} solution:\n {solution}\n\n')