#!/usr/bin/python3

import sys, os, os.path, re, json
import math, random

PRONOUNS = [
        "yo", "tú", "él/ella/usted", "nosotros", "vosotros", "ellos/ellas/ustedes"
        ]

def load_verbs(verb_collection, verb_set_name):
    for f in os.listdir("."):
        m = re.match("^verbs-%s-(.*)\.txt$" % verb_set_name, f)
        if m:
            subset_name = m.groups(1)[0]
            with open(f) as fd:
                lines = fd.readlines()
            for ln in lines:
                pcs = ln.rstrip().split(":")
                inf = pcs[1]
                cnj = pcs[2:]
                if inf not in verb_collection:
                    verb_collection[inf] = {}
                verb_collection[inf][subset_name] = cnj

def print_verb_definitions():
    vs = {}
    load_verbs(vs, "ar")
    for v in vs:
        print(v, vs[v])

def generate_worksheet_data(dst):
    N_REPS = 3
    BLANK_COUNT = 20
    verbs = {}
    load_verbs(verbs, "ar")
    # Reference
    problems = []
    for v in verbs:
        print(v, file=dst)
        for i in range(len(PRONOUNS)):
            print("%s %s" % (PRONOUNS[i], verbs[v]["present"][i]), file=dst)
            pros = PRONOUNS[i].split("/")
            for z in range(N_REPS):
                pro = random.choice(pros)
                problems.append("%s + %s = %s" % (pro, v, "_" * BLANK_COUNT))
        print("", file=dst)
    random.shuffle(problems)
    for p in problems:
        print("", file=dst)
        print(p, file=dst)

if __name__ == "__main__":
    random.seed()
    #print_verb_definitions()
    with open("/home/nate/verbs.txt", "w", encoding="latin-1") as f:
        generate_worksheet_data(f)

