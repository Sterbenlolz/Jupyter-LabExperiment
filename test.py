from sympy import *

a = 0
z1 = 50
z2 = 100
z3 = 150
U1 = 10
U2 = 110
U3 = 30
r1 = 10
r2 = 10
r3 = 10
r, z, U = symbols('r z U')
E1 = (U1 - U2) / (z2 - z1)
E2 = (U2 - U3) / (z3 - z2)
E0 = (-U1) / z1
E3 = U3 / z1

form1 = f'((0 - {U1}) / (0 - {z1})) * z'
form2 = f'{U1} + ({r1} / pi) * ({E0} - {E1}) * (1 + (Abs(z - {z1}) / {r1}) * atan(Abs(z - {z1}) / {r1})) - 0.5 * (z - {z1}) * ({E0} + {E1})'
form4 = f'{U2} + ({r2} / pi) * ({E1} - {E2}) * (1 + (Abs(z - {z2}) / {r2}) * atan(Abs(z - {z2}) / {r2})) - 0.5 * (z - {z2}) * ({E1} + {E2})'
form6 = f'{U3} + ({r3} / pi) * ({E2} - {E3}) * (1 + (Abs(z - {z3}) / {r3}) * atan(Abs(z - {z3}) / {r3})) - 0.5 * (z - {z3}) * ({E2} + {E3})'
form7 = f'(({U3} - 0) / (0 - {z1})) * z - ({z3} * {U3}) / (0 - {z1})'
f1 = sympify(form1)
f2 = sympify(form2)
f3 = sympify(form3)
f4 = sympify(form4)
f5 = sympify(form5)
f6 = sympify(form6)
f7 = sympify(form7)


file = open('testing.csv', 'w')



while  a < z3:
    values = []
    func = f4.evalf(subs={z: a})
    values.append(func)
    func = f3.evalf(subs={z: a})
    values.append(func)
    func = f2.evalf(subs={z: a})
    values.append(func)
    for i in values:
        file.write(str(i) + ', ')
    file.write('\n')
    a += 1

