from constraint import *

def different(a,b):
    return a != b

if __name__ == "__main__":
    problem = Problem()

    variables = ["WA", "NT", "SA", "Q", "V", "NSW"]
    domain = ["red", "green", "blue"]

    problem.addVariables(variables, domain)

    problem.addConstraint(different, ("WA", "NT"))
    problem.addConstraint(different, ("WA", "SA"))
    problem.addConstraint(different, ("SA", "NT"))
    problem.addConstraint(different, ("SA", "NSW"))
    problem.addConstraint(different, ("SA", "Q"))
    problem.addConstraint(different, ("SA", "V"))
    problem.addConstraint(different, ("NT", "Q"))
    problem.addConstraint(different, ("NSW", "NT"))

    solutions = problem.getSolutions()

    print(solutions)