import gurobipy as gp

def first_problem():
    m = gp.Model()

    x1 = m.addVar(vtype='C', name="x1")
    x2 = m.addVar(vtype='C', name="x2")
    x3 = m.addVar(vtype='C', name="x3")
    x4 = m.addVar(vtype='C', name="x4")

    m.setObjective(x1 + 3 * x2 + x3, gp.GRB.MINIMIZE)

    m.addConstr(2 * x1 + x2 + 3 * x3 == 35)
    m.addConstr(-x1 + x2 + 2 * x4 == 12)

    m.addConstr(x1 >= 0)
    m.addConstr(x2 >= 0)
    m.addConstr(x3 >= 0)
    m.addConstr(x4 >= 0)

    m.optimize()

    print(f"Optimal objective value: {m.objVal}")
    print(f"Solution values: x1={x1.X}, x2={x2.X}, x3={x3.X}, x4={x4.X}")

def second_problem():
    m = gp.Model()

    x1 = m.addVar(vtype='C', name="x1")
    x2 = m.addVar(vtype='C', name="x2")
    x3 = m.addVar(vtype='C', name="x3")
    x4 = m.addVar(vtype='C', name="x4")
    x5 = m.addVar(vtype='C', name="x5")
    x6 = m.addVar(vtype='C', name="x6")

    m.setObjective(-2 * x1 - x2, gp.GRB.MINIMIZE)

    m.addConstr(2 * x1 + x2 + 2 * x3 == 4)
    m.addConstr(2 * x1 + 3 * x2 + x4 == 3)
    m.addConstr(4 * x1 + x2 + 3 * x5 == 5)
    m.addConstr(x1 + 5 * x2 + x6 == 2)

    m.addConstr(x1 >= 0)
    m.addConstr(x2 >= 0)
    m.addConstr(x3 >= 0)
    m.addConstr(x4 >= 0)
    m.addConstr(x5 >= 0)
    m.addConstr(x6 >= 0)

    m.optimize()

    print(f"Optimal objective value: {m.objVal}")
    print(f"Solution values: x1={x1.X}, x2={x2.X}, x3={x3.X}, x4={x4.X}, x5={x5.X}, x6={x6.X}")

if __name__ == "__main__":
    first_problem()
    second_problem()