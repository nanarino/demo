#解二元一次方程组
def solve(eq1, eq2, var=('x', 'y')):
    eq1 = eq1.replace("=", "-(") + ")"
    eq1_x0 = eval(eq1, {var[0]: 1j, var[1]: 0})
    eq1_y0 = eval(eq1, {var[0]: 0, var[1]: 1j})
    #斜率
    eq1_a = -(eq1_x0.imag) / (eq1_y0.imag)
    #相位
    eq1_b = -eq1_y0.real / eq1_y0.imag
    eq2 = eq2.replace("=", "-(") + ")"
    eq2 = eval(eq2.replace(var[1], "({0}*x+{1})".format(*[eq1_a, eq1_b])),
               {var[0]: 1j})
    x = -eq2.real / eq2.imag
    y = eq1_a * x + eq1_b
    return "{}={};{}={}".format(var[0], x, var[1], y)


print(solve('x+y=10', '2*x+4*y=16'))
