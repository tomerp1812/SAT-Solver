import sys
import time
from naive_solver import naive_solve
from dpll_solver import dpll_solve

# in what follows, a *formula* is a collection of clauses,
# a clause is a collection of literals,
# and a literal is a non-zero integer.

# input path:  a path to a cnf file
# output: the formula represented by the file, 
#         the number of variables, 
#         and the number of clauses
def parse_dimacs_path(path):
    data = []
    row = []
    with open(path, 'r') as file:
        first_line = file.readline()
        split = first_line.split(' ')
        num_of_rows = int(split[2])
        num_of_clauses = int(split[3].split('\n')[0])
        for line in file.readlines():
            if line == '\n':
                break
            tmp = line.split('\n')[0]
            numbers = tmp.split(' ')
            for num in numbers:
                if num != '' and num != '0' and (num.isdigit() or (num[0] == '-' and num[1:].isdigit())):
                    row.append(int(num))
            data.append(row)
            row = []
    return data, num_of_rows, num_of_clauses


def main():
    # get path to cnf file from the command line
    path = sys.argv[1]

    # parse the file
    cnf, num_vars, num_clauses = parse_dimacs_path(path)

    # dpll algorithm
    start = time.time()
    dpll_solve(cnf, num_vars, num_clauses)
    end = time.time()
    print("DPLL Time:", end - start)

    # naive algorithm
    start = time.time()
    naive_solve(cnf, num_vars, num_clauses)
    end = time.time()
    print("Naive Time:", end - start)




if __name__ == "__main__":
    main()