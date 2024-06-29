# importing system module for reading files
import sys
import time

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


# input cnf: a formula
# input n_vars: the number of variables in the formula
# input n_clauses: the number of clauses in the formula
# output: True if cnf is satisfiable, False otherwise
def naive_solve(cnf, n_vars, n_clauses):
    assignment = [False] * n_vars
    for i in range(2 ** n_vars):
        b = bin(i)
        for j in range(len(b) - 1, 1, -1):
            if b[j] == '1':
                assignment[len(b) - 1 - j] = True
            else:
                assignment[len(b) - 1 - j] = False
        if all(is_clause_satisfied(clause, assignment) for clause in cnf):
            print("sat")
            for index in range(len(assignment)):
                print(f"{index + 1}:", assignment[index])
            return

    print("unsat")
    return []


def is_clause_satisfied(clause, assignment):
    for literal in clause:
        if literal > 0 and assignment[literal - 1]:
            return True
        elif literal < 0 and not assignment[-literal - 1]:
            return True
    return False


def decide(m, f):
    if m:
        for row in f:
            for literal in row:
                if literal not in m and literal * (-1) not in m:
                    return literal
    else:
        return f[0][0]
    return 0


def backtrack(m, literal, n, f, d):
    counter = 0
    if d:
        if literal in d:
            for i in n:
                if i in d:
                    return 0
            for row in f:
                for lit in row:
                    if lit * (-1) in m:
                        counter = counter + 1
                    else:
                        counter = 0
                        break
                if counter == len(row):
                    m.remove(literal)
                    for num in n:
                        m.remove(num)
                    m.append(literal * (-1))
                    d.remove(literal)
                    if d:
                        new_guess = d[-1]
                        index = m.index(new_guess)
                        n = m[index + 1:]
                    else:
                        n = []
                        new_guess = 0
                    return m, new_guess, n, d, True

    return m, literal, n, d, False


def unit_propagate(m, f, d):
    counter = 0
    x = 0
    if m:
        for row in f:
            for literal in row:
                if literal * (-1) in m:
                    counter = counter + 1
                else:
                    x = literal
            if len(row) == counter + 1:
                if x not in m and x != 0:
                    return x
            counter = 0
            x = 0
    else:
        for row in f:
            if len(row) == 1:
                return row[0]
    return 0


def fail(m, f, d):
    counter = 0
    if not d:
        for row in f:
            for literal in row:
                if literal * (-1) in m:
                    counter += 1
                else:
                    counter = 0
                    break
            if counter == len(row):
                return True
    return False


# input cnf: a formula
# input n_vars: the number of variables in the formula
# input n_clauses: the number of clauses in the formula
# output: True if cnf is satisfiable, False otherwise
def dpll_solve(cnf, n_vars, n_clauses):
    if not cnf:
        return True
    m = []
    d = []
    f = cnf
    n = []
    literal = 0
    while True:
        """ UNIT PROPAGATE """
        x = unit_propagate(m, f, d)
        if x != 0:
            m.append(x)
            n.append(x)
            continue
        """ BACKTRACK """
        m, literal, n, d, boolean = backtrack(m, literal, n, f, d)
        if boolean:
            continue
        """ DECIDE """
        x = decide(m, f)
        if x != 0:
            m.append(x)
            d.append(x)
            literal = x
            n = []
            continue
        """ FAIL """
        if fail(m, f, d):
            print("unsat")
            return False
        else:
            print("sat")
            assignment = [False] * len(m)
            for num in m:
                if num > 0:
                    assignment[num - 1] = True
            for i in range(len(assignment)):
                print(f"{i + 1}:", assignment[i])
            return True

    ######################################################################


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