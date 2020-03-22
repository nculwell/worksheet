#!/usr/bin/python3

import sys, os, os.path, re, json
import math, random

PRONOUNS = [
        "yo", "tú", "él/ella/usted", "nosotros", "vosotros", "ellos/ellas/ustedes"
        ]

BLANK_COUNT = 20
BLANK = "_" * BLANK_COUNT
N_REPS = 3

def generate_worksheet_data(dst, infinitives):
    problems = [ [] for z in range(N_REPS * 2) ]
    infinitives_midpoint = int(len(infinitives) / 2)
    infs_split = infinitives[:infinitives_midpoint], infinitives[infinitives_midpoint:]
    print(infs_split)
    for inf_set_i in [0, 1]:
        for inf in infs_split[inf_set_i]:
            for i in range(len(PRONOUNS)):
                pros = PRONOUNS[i].split("/")
                for z in range(N_REPS):
                    problem_index = z * 2 + inf_set_i
                    pro = random.choice(pros)
                    problems[problem_index].append("%s + %s = %s" % (pro, inf, BLANK))
    for z in range(N_REPS * 2):
        random.shuffle(problems[z])
    for z in range(N_REPS * 2):
        for p in problems[z]:
            print("", file=dst)
            print(p, file=dst)

if __name__ == "__main__":
    infinitives = sys.argv[1:]
    random.seed()
    #print_verb_definitions()
    with open("/home/nate/verb_worksheet.txt", "w", encoding="latin-1") as f:
        generate_worksheet_data(f, infinitives)

