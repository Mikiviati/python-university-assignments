def Pareto(*pairs):
    return tuple(p for p in pairs if not any(p[0] <= q[0] and p[1] <= q[1] and (p[0] < q[0] or p[1] < q[1]) for q in pairs))

print(Pareto(*tuple(eval(input()))))
