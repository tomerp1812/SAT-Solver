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