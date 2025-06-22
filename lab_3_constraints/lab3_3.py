from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    lectures_AI = input()
    lectures_ML = input()
    lectures_R = input()
    lectures_BI = input()

    AI_lectures_domain = ["Mon_11", "Mon_12", "Wed_11", "Wed_12", "Fri_11", "Fri_12"]
    ML_lectures_domain = ["Mon_12", "Mon_13", "Mon_15", "Wed_12", "Wed_13", "Wed_15", "Fri_11", "Fri_12", "Fri_15"]
    R_lectures_domain = ["Mon_10", "Mon_11", "Mon_12", "Mon_13", "Mon_14", "Mon_15", "Wed_10", "Wed_11", "Wed_12",
                         "Wed_13", "Wed_14", "Wed_15", "Fri_10", "Fri_11", "Fri_12", "Fri_13", "Fri_14", "Fri_15"]
    BI_lectures_domain = ["Mon_10", "Mon_11", "Wed_10", "Wed_11", "Fri_10", "Fri_11"]

    AI_tutorials_domain = ["Tue_10", "Tue_11", "Tue_12", "Tue_13", "Thu_10", "Thu_11", "Thu_12", "Thu_13"]
    ML_tutorials_domain = ["Tue_11", "Tue_13", "Tue_14", "Thu_11", "Thu_13", "Thu_14"]
    BI_tutorials_domain = ["Tue_10", "Tue_11", "Thu_10", "Thu_11"]

    # ---Add the variables here--------------------
        
    # ---Add the constrains here----------------
    # ----------------------------------------------------
    solution = problem.getSolution()

    print(solution)