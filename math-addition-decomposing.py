#!/usr/bin/python3

import sys, os, os.path, re, json
import math, random

PROBLEM_COUNT = 40
BLANK_WIDTH = 5
blank = "_" * BLANK_WIDTH

def divide_place_value(n):
    nTens = [ 10*int(x/10) for x in n ]
    nOnes = [ x % 10 for x in n ]
    return nTens, nOnes

def generate_problems():
    problems = []
    #for problem_number in range(problem_count):
    while True:
        problem = []
        n = [ random.randint(10, 99) for i in range(2) ]
        nTens, nOnes = divide_place_value(n)
        problem.append(n + [sum(n)])
        for i in range(2):
            problem.append([ nTens[i], nOnes[i], n[i] ])
        problem.append([ nOnes[0], nOnes[1], sum(nOnes) ])
        problem.append([ nTens[0], nTens[1], sum(nTens) ])
        problem.append([ sum(nOnes), sum(nTens), sum(nOnes + nTens) ])
        yield problem

def problem_requires_carrying(problem):
    n = problem[0][0:2]
    nTens, nOnes = divide_place_value(n)
    return (sum(nTens) >= 100 or sum(nOnes) >= 10)

def problem_has_zeros(problem):
    n = problem[0][0:2]
    nTens, nOnes = divide_place_value(n)
    return nOnes[0] == 0 or nOnes[1] == 0

def print_problem(f, problem_number, problem):
    print("%d." % problem_number, file=f)
    for line in problem:
        values = tuple([ "%3d" % x if not x is None else blank for x in line ])
        print("%s + %s = %s" % values, file=f)
    print(file=f)

def print_problems(f):
    problem_number = 0
    for problem in generate_problems():
        if problem_number <= 30 and problem_requires_carrying(problem):
            continue
        if problem_number < 2 and problem_has_zeros(problem):
            continue
        problem_number = problem_number + 1
        fuzz_level = int((problem_number - 2) / 3)
        if fuzz_level < 0:
            fuzz_level = 0
        problem = fuzz(fuzz_level, problem)
        print_problem(f, problem_number, problem)
        if problem_number == PROBLEM_COUNT:
            break

def fuzz(fuzz_level, problem):
    problem = [ [ y for y in x ] for x in problem ] # copy problem
    n_lines = len(problem)
    if fuzz_level < n_lines:
        # Add random blanks.
        lines_for_blanks = random.sample(range(n_lines), fuzz_level)
        for i in lines_for_blanks:
            j = random.randrange(3)
            problem[i][j] = None
    else:
        # Blank out all but the first 2 numbers.
        problem[0][2] = None
        for i in range(1, n_lines):
            problem[i] = [ None, None, None ]
    return problem

if __name__ == "__main__":
    random.seed()
    with open("/home/nate/math-addition-decomposing.txt", "w", encoding="latin-1") as f:
        print_problems(f)

