from constraint import *

def arithmeticEquation(s,e,n,d,m,o,r,y):
    send = 1000*s + 100 * e + 10 * n + d
    more = 1000*m + 100 * o + 10 * r + e
    money = 10000 * m + 1000 * o + 100 * n + 10*e + y
    return send+more == money

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    variables = ["S", "E", "N", "D", "M", "O", "R", "Y"]
    for variable in variables:
        problem.addVariable(variable, Domain(set(range(10))))

    # ---Add the constraints here----------------
    problem.addConstraint(AllDifferentConstraint(), variables)
    problem.addConstraint(arithmeticEquation, variables)
    # ----------------------------------------------------

    print(problem.getSolution())