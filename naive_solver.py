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